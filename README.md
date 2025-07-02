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

---







