# ChatMate: Your Chat Buddy 🤖💬

**ChatMate** is a lightweight pocket chatbot designed to run efficiently even without high-end hardware. Built using the **Orca Mini 3B** model, this project showcases how small LLMs can be deployed effectively for interactive chat applications. It is fully executable inside **GitHub Codespaces**, making it accessible and portable.


![image](https://github.com/user-attachments/assets/5c9deb94-56d0-4666-a53b-27486aec770c)


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
Create a `Model/orca_mini` directory and download the model using: "wget https://huggingface.co/zoltanctoth/orca_mini_3B-GGUF/resolve/main/orca-mini-3b.q4_0.gguf"

> > 📦 **Why the model isn't included**:  
Due to GitHub's 2GB file upload limit, the Orca Mini 3B model is **not uploaded to this repository**.  

> 🧠 **Model Loading**:  
Used **CTransformers** to load the model due to its lighter weight compared to `llama-cpp`. But to `FinTer.py` used `llama-cpp`.

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

Due to GitHub’s file upload size limitations, the **Orca Mini 3B model is not included** in this repository.

To run the project:
1. Manually create a `Model/orca_mini/` directory.
2. Inside that folder, run the following command:
   ```bash
   wget https://huggingface.co/zoltanctoth/orca_mini_3B-GGUF/resolve/main/orca-mini-3b.q4_0.gguf

