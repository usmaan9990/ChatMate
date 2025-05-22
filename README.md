# ChatMate: Your Chat Buddy 🤖💬

**ChatMate** is a lightweight pocket chatbot designed to run efficiently even without high-end hardware. Built using the **Orca Mini 3B** model, this project showcases how small LLMs can be deployed effectively for interactive chat applications. It is fully executable inside **GitHub Codespaces**, making it accessible and portable.

---

## 💡 Key Features

- 💬 Uses the **Orca Mini 3B** model for conversational AI.
- 🚀 Runs entirely inside **GitHub Codespaces** (no local GPU required).
- ⚡ Loaded using **CTransformers** – lightweight alternative to Llama.cpp.
- 🌐 Built with **Flask** for easy interaction via web browser.
- 📁 Model sourced from Hugging Face and integrated via `ctransformers`.

---

## ⚙️ Project Setup (Key Notes)

> 📝 **Model Setup**:  
Create a `models/orca_mini` directory and download the model using: "wget https://huggingface.co/zoltanctoth/orca_mini_3B-GGUF/resolve/main/orca-mini-3b.q4_0.gguf"

> 🧠 **Model Loading**:  
Used **CTransformers** to load the model due to its lighter weight compared to `llama-cpp`.

> 🌐 **App Backend**:  
Implemented using **Flask** to serve the chatbot interface.

> 🧑‍💻 **Platform**:  
Project built and executed using **GitHub Codespaces** – no powerful local hardware is needed.

---

## 🧪 Experimental Script: `FinTer.py`

The repository also includes an experimental script named **`FinTer.py`**, where I tested the **DeepSeek Coder 1.3B Base** model:

- 📌 Model used: [`deepseek-coder-1.3b-base-GGUF`](https://huggingface.co/TheBloke/deepseek-coder-1.3b-base-GGUF)
- 🧪 Purpose: Only for trying out another LLM (not a complete app).
- ⚠️ Limitation: Due to hardware constraints, this script was not extended into a full application.

---

## 🙏 Credits

- 👨‍🏫 **Lecturer**: Special thanks to **Zoltan C. Toth** for the Orca Mini model and foundational teaching.
- 📚 Tutorials and personal course learnings contributed to the development of this project.

---

## 📄 License & Usage

This project is created for educational purposes. Please refer to the license terms of the respective models on Hugging Face.

---

## 📌 Note

This is a learning project intended to demonstrate how to integrate small LLMs in real-world scenarios using limited resources. While **ChatMate** is a basic chatbot, it sets the groundwork for future enhancements including memory support, rich UI, and deployment to mobile/web platforms.

