# 🌌 AstroVision – Astrology Web Application

AstroVision is a modern Django-based astrology web application that provides instant zodiac predictions, daily & weekly horoscopes, and astrology insights with a premium UI and secure authentication system.

---
## ✨ Features
* 🔐 User Authentication (Sign Up / Login / Logout)
* 🏠 Protected Dashboard (Login Required)
* ♈ Zodiac Sign Detection from Birth Date
* ⏰ Birth Time Category Analysis
* 🔮 Instant Personalized Prediction
* 🌞 Daily Horoscope Page
* 📅 Weekly Horoscope Page
* 🧠 Astrology Knowledge Blog (Sun, Moon, Nakshatra)
* 🎨 Premium Glassmorphism UI
* 📱 Fully Responsive Design
* 🔁 Re-check Predictions

---
## 🛠️ Tech Stack
* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite (Default Django DB)
* **Authentication:** Django Built-in Auth
* **UI Style:** Glassmorphism + Dark Premium Theme
---
## 🚀 How to Clone and Run This Project
### 1. Clone the Repository

```bash
git clone <your-repo-link>
cd astro
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

---

### 3. Activate Virtual Environment

**For Windows (PowerShell):**

```bash
venv\Scripts\activate
```

**For Mac/Linux:**

```bash
source venv/bin/activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not available:

```bash
pip install django
```

---

### 5. Navigate to Project Folder

⚠️ Make sure you are inside the folder where `manage.py` exists

```bash
cd astro_project
```

---

### 6. Run Migrations

```bash
python manage.py migrate
```

---

### 7. Start Development Server

```bash
python manage.py runserver
```

---

### 8. Open in Browser

```
http://127.0.0.1:8000/
```

---

## ⚠️ Important Notes

* Always run commands from the folder containing `manage.py`
* Activate virtual environment before running the server
* This is a development server (not for production)

---

## 🛠️ Common Error Fix

### ❌ Error:

```
can't open file 'manage.py'
```

### ✅ Solution:

You are in the wrong directory. Run:

```bash
cd astro_project
```

---

## 📁 Project Structure

```
astro/
│
├── astro_project/   # Main Django project (contains manage.py)
├── venv/            # Virtual environment
└── README.md
```
