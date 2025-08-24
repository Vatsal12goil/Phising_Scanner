# 🛡️ Phishing Link Scanner

A lightweight **Phishing Link Scanner** built using Python (and optional frontend with HTML/CSS/JS).  
This tool analyzes suspicious URLs to detect whether they are **legitimate or potentially malicious** using rule-based checks and/or machine learning models.  

---

## 🚀 Features
- 🔗 Input any URL and check for phishing characteristics  
- 🧾 Detects common phishing indicators such as:  
  - Use of IP address instead of domain  
  - Suspicious domain length  
  - Presence of `@` symbol, `-`, or unusual subdomains  
  - HTTPS verification  
  - URL redirection  
- ⚡ Fast and lightweight – scans in seconds  
- 🎨 Can be extended with a simple web frontend  

---

## 📂 Project Structure
├── phishing_scanner.py # Core Python script
├── dataset.csv # (Optional) Training dataset for ML
├── model.pkl # (Optional) Trained ML model
├── templates/ # (For Flask/Django frontend)
│ └── index.html
├── static/ # CSS, JS, icons
├── requirements.txt # Dependencies
└── README.md # Documentation


2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the scanner
python phishing_scanner.py


For Web Version (Flask example):

python app.py


Then open browser at http://127.0.0.1:5000/



📦 Requirements

Python 3.x

Libraries: scikit-learn, pandas, numpy, flask (for web)
