# fooddonationsystem
A Flask-based web application that allows users to donate leftover food and view available donations. Built using Python, MySQL, HTML, CSS, and Flask without XAMPP.
# 🍱 Food Donation System

A **Flask-based web application** that helps connect food donors with those in need.  
Users can **add, view, and delete food donations** with details such as donor name, quantity, and pickup address.  
This project uses **Python, Flask, MySQL, HTML, and CSS** — developed entirely using **VS Code, CMD, and MySQL server** (no XAMPP).

---

## 🚀 Features
- Add new food donations through a simple web form.
- View all active donations in a clean table layout.
- Delete donations safely with confirmation prompts.
- Connected to MySQL database using `mysql-connector-python`.
- Fully responsive front-end with custom CSS.

---

## 🛠️ Tech Stack
| Component | Technology |
|------------|-------------|
| Language | Python 3 |
| Framework | Flask |
| Database | MySQL |
| Frontend | HTML, CSS |
| IDE | Visual Studio Code |
| Tools | Command Prompt, MySQL Server |

---

## ⚙️ Setup Instructions

# 1️⃣ Clone this repository
git clone https://github.com/<your-username>/FoodDonationSystem.git
cd FoodDonationSystem

# 2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the app
python app.py

#Folder Structure
FoodDonationSystem/
├── app.py
├── models.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── add.html
├── static/
│   └── style.css
└── venv/
