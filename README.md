# 🚀 AI Brand Studio – Generative Poster & Logo Creator

AI Brand Studio is a Flask-based web application that generates AI-powered brand-style visuals using Stable Diffusion (SD-Turbo) for real-time image synthesis.

The application allows users to enter prompts and dynamically generates AI-designed backgrounds with structured text overlay rendering.

This project demonstrates end-to-end AI model integration within a web application architecture.

---

## ✨ Features

- 🧠 Real-time AI image generation using Stable Diffusion (SD-Turbo)
- 🎨 Dynamic prompt-based visual creation
- 📝 Text overlay rendering using PIL (Pillow)
- 🌐 Interactive web interface
- ⚡ Fast local inference pipeline
- 🛠 Modular Flask backend structure
- 📦 Clean, Git-ready project setup

---

## 🛠 Tech Stack

### Backend
- Python
- Flask
- PyTorch
- HuggingFace Diffusers

### Frontend
- HTML
- CSS
- JavaScript

### Image Processing
- PIL (Pillow)

### Version Control
- Git & GitHub

---

## 📂 Project Structure

```
ai-brand-studio/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── generated/
│
└── templates/
    └── index.html
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-brand-studio.git
cd ai-brand-studio
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
python app.py
```

Then open:

http://127.0.0.1:5000

---

## 🧠 How It Works

1. User enters a design prompt
2. Backend sends prompt to Stable Diffusion (SD-Turbo) pipeline
3. Model generates background image
4. PIL overlays custom brand text
5. Generated image is served dynamically to frontend

---

## 🚀 Future Improvements

- Higher-quality diffusion models
- Cloud deployment (Render / Railway / HuggingFace Spaces)
- User authentication
- Image history storage
- Downloadable high-resolution images

---

## 📌 Why This Project?

This project showcases:

- AI model integration inside a web application
- Backend–frontend communication
- Real-time generative inference
- Clean software project structure
- Practical deployment preparation

---

## 📜 License

This project is open-source and available for educational and personal use.