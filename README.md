<h1 align="center">🕒 Daily Date-Time</h1>

<p align="center">
  A beginner-friendly Python script that displays the current <strong>date</strong>, <strong>time</strong>, and a context-aware <strong>greeting</strong>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue?style=flat-square">
  <img src="https://img.shields.io/github/last-commit/Daud-Nisar/daily-date-time?style=flat-square">
  <img src="https://img.shields.io/github/repo-size/Daud-Nisar/daily-date-time?style=flat-square">
</p>

---

## 📌 Overview

This script prints the current date and time based on your local machine’s clock and gives a greeting like:

- ☀️ Good Morning (before 12 PM)
- 🌤️ Good Afternoon (12 PM – 5 PM)
- 🌙 Good Evening (after 5 PM)

It’s a simple project made to practice Python basics, working with `datetime`, and printing clean output.

---

## 🖼️ Sample Output

📅 Date: Tuesday, 02 July 2025
🕒 Time: 10:23:45 AM
👋 Good Morning ☀️

---

## 💻 How to Use

### 1. Clone or Download the Repository
```bash
git clone https://github.com/Daud-Nisar/daily-date-time.git
cd daily-date-time

### 2. Run the Script
Make sure Python is installed, then:
python main.py

### 🔍 Code Breakdown (main.py)
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%I:%M:%S %p")
current_date = now.strftime("%A, %d %B %Y")
hour = now.hour

if hour < 12:
    greeting = "Good Morning ☀️"
elif 12 <= hour < 17:
    greeting = "Good Afternoon 🌤️"
else:
    greeting = "Good Evening 🌙"

print("📅 Date:", current_date)
print("🕒 Time:", current_time)
print("👋", greeting)


### 🚀 Future Improvements
-  Add GUI using Tkinter
- Save output to a .txt file
- Auto-push current time daily to GitHub using GitHub Actions
-  Add support for other timezones

## 🙋‍♂️ About Me
Daud Nisar — Python Developer from Pakistan 🇵🇰
💼 Specializing in:
- Python Scripts & Automation
- Web Scraping
- QA Testing with Selenium

## 🔗 Connect with Me

[💻 GitHub](https://github.com/Daud-Nisar) | [💼 LinkedIn](https://www.linkedin.com/in/daud-nisar-aa88a9222/) | [🧰 Upwork](https://www.upwork.com/freelancers/~0152296150762df3c8?mp_source=share)

## ⭐️ Support

If you liked this project:

- ⭐️ Star this repository  
- ✅ Follow me on [GitHub](https://github.com/Daud-Nisar)  
- 💬 Share your feedback or suggest improvements





