# Visual Question Answering (VQA) App

A simple **Multimodal AI project** that uses **BLIP (Vision-Language Transformer)** and **Gradio** to answer questions about images.  
This project demonstrates **how AI can understand both images and text simultaneously** to provide meaningful answers.

---

## 🚀 Features

- Upload any image and ask a question about it.  
- Get text-based answers using a pre-trained **BLIP model**.  
- Fast and accurate using **Torch + Torchvision** for image processing.  
- Built with **Python** and a simple **Gradio web interface**.  

---

## 🖥️ Demo

Example questions you can ask:

- What is the person doing in this image?  
- What objects are visible?  
- What animal is shown in the image?  
- Is this indoors or outdoors?  
- Describe the scene.  
- What is the color of the object?  

> Works best with clear images and simple questions.

---

## 🛠️ Technologies & Libraries Used

- **Python 3.10+**  
- **PyTorch** – Deep learning framework  
- **Torchvision** – Image processing  
- **Transformers** – Pre-trained BLIP model  
- **Gradio** – Easy-to-use web interface  
- **Pillow (PIL)** – Image handling  

---

## 📁 Project Structure
PythonProject6/
│
├─ app.py # Main VQA app code
├─ requirements.txt # Python dependencies
├─ README.md # Project documentation
└─ .gitignore # Ignore virtualenv and cache files

---

## ⚡ Installation

1. Clone the repository:

```bash
git clone https://github.com/YOURUSERNAME/Visual-Question-Answering-App.git
cd Visual-Question-Answering-App

2.Install dependencies:

python -m pip install -r requirements.txt


3.Run the app:

python app.py