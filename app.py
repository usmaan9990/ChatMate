from flask import Flask, render_template, request, redirect, url_for
from ctransformers import AutoModelForCausalLM

app = Flask(__name__)


llm = AutoModelForCausalLM.from_pretrained("Model/orca_mini",model_file="orca-mini-3b.q4_0.gguf")


chat_history = [] 

def get_prompt(instruction: str, history: list[str] | None = None) -> str:
    system = "Hi you are an AI assistant, who will give helpful and proper answer very clearly."
    prompt = f"### System:\n{system}\n"
    if history is not None:     
        prompt += f"This is the conversation history before this chat: {' '.join(history)}. Now answer the question: "
    prompt += f"\n### User:\n{instruction}\n\n"
    return prompt

@app.route("/", methods=["GET", "POST"])
def chat():
    global chat_history
    if request.method == "POST":
        user_input = request.form["message"]
        prompt = get_prompt(user_input, chat_history)

        response = ""
        model_output = llm(prompt)

        for token in model_output:
            response += token

        chat_history.append(f"User: {user_input}")
        chat_history.append(f"ChatMate: {response}")

        return redirect("/")

    return render_template("index.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)
