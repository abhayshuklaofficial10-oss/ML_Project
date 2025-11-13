# 🎓 Student Math Score Prediction App

An interactive **Flask web application** that predicts a student's **math score** based on gender, parental education, lunch type, test preparation, and reading/writing scores using a **Machine Learning model**.

---

## 🚀 Features
- 🎯 Predict math score based on user input  
- 💡 Machine Learning model integrated with Flask  
- 🧠 Data preprocessing and scaling pipeline  
- 💻 Beautiful Tailwind CSS UI  
- 📊 Real-time prediction display  

---

## 🧰 Tech Stack

| Category | Technologies |
|-----------|--------------|
| **Backend** | Python, Flask |
| **Machine Learning** | Scikit-learn, NumPy, Pandas |
| **Frontend** | HTML5, Tailwind CSS |
| **Deployment** | Render / AWS / Heroku *(optional)* |

---

## 📁 Project Structure

📦 Student_Math_Score_Prediction
├── src/
│ ├── components/
│ ├── pipeline/
│ ├── exception.py
│ ├── logger.py
│ └── utils.py
├── templates/
│ └── home.html
├── static/ # (optional, if you add custom CSS/JS)
├── app.py # Flask main file
├── requirements.txt
├── README.md
└── artifact/ # stores model artifacts and datasets


---
## 🖼️ Screenshot

<p align="center">
  <img src="https://github.com/abhayshuklaofficial10-oss/ML_Project/blob/main/Screenshot%20(239).png?raw=true" alt="Student Math Score Predictor UI" width="800">
</p>

> 🧠 Beautiful one-page, scroll-free Tailwind UI.

## ⚙️ Installation and Run Instructions

### **1️⃣ Clone the repository**
```bash
git clone https://github.com/<your-username>/student-math-score-predictor.git
cd student-math-score-predictor

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS / Linux
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python app.py

```bash








