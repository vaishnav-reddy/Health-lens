# 🌟 Health-Lens

**Health-Lens** is a simple AI-powered medical analysis web application.  
It allows users to interact with an interface that provides diagnostic support and insights for health conditions using uploaded images and AI logic.  
The frontend is based on pure HTML/CSS/JS and the backend has Python logic to process and predict results.



---

## 🧠 Project Overview

Health-Lens is designed to offer:

✨ AI-based health diagnostics  
📸 Image upload interface  
🚀 Quick prediction results  
🧑‍⚕️ Simple UI for non-technical users

This application provides a starting point for building a more advanced machine learning-driven healthcare tool.

---

### 📁 Repository Structure

Health-lens/
├──.streamlit
    ├──.streamlit
         ├──secrets.toml
├── home.html # Main UI page
├── style.css # Frontend styles
├── script.js # Frontend JavaScript
├── medico.py # Backend Python logic
├── requirements.txt # Python dependencies
├── user1.jpg # Example/test image
├── user2.jpg
├── user3.jpeg
├── healthvideo1.mp4 # Demo video files
├── healthvideo2.mp4
├── .gitignore



Files like `home.html`, `style.css`, and `script.js` form the web interface.  
`medico.py` contains the Python backend logic for processing image uploads and returning predictions. 

---

## 🚀 Features

✔ Intuitive image upload  
✔ Clean web UI  
✔ Backend Python logic for predictions  
✔ Easy to deploy or customize further  
✔ Can be extended with real AI/ML models  

---

## 📦 Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend  | HTML, CSS, JavaScript |
| Backend   | Python |
| Hosting   | Netlify (Frontend) ,Streamlit(Backend)|
| AI Logic  | Python backend (can be expanded) | 

---
### 🔐 IMPORTANT — API KEY REQUIREMENT

This project WILL NOT RUN unless you create the following file:

.streamlit/secrets.toml


Inside it, you must add your API key like this:

api_key = "YOUR_API_KEY_HERE"


If this file is missing, the backend cannot connect to the API, and the app will not work.

## 🛠️ Setup & Installation

### 1️⃣ Clone the Project

```bash
git clone https://github.com/vaishnav-reddy/Health-lens.git

```
cd Health-lens

### 2️⃣ Install Backend Dependencies

Create a Python environment and install:

pip install -r requirements.txt

### 3️⃣ Run Backend

python -m streamlit run medico.py

This starts your Python logic.

### 4️⃣ Open Frontend

Open home.html in your browser

Or deploy to a static host (Netlify, GitHub Pages, Firebase Hosting, etc.).

### 📸 How to Use

Open the web UI

Upload an image

Click Submit

View AI inference results

(Current logic uses Python backend — extend with real AI model as needed.)

### 👉 Future Enhancements

✅ Replace basic logic with real ML model
✅ Add Docker support
✅ Integrate proper API backend
✅ Improve UI responsiveness
✅ Add multiple disease classifications

### 📝 License

This project is open-source and free to modify for learning and development purposes.
Feel free to fork and contribute!

### 👨‍💻 Author

Vaishnav Reddy
GitHub: https://github.com/vaishnav-reddy

