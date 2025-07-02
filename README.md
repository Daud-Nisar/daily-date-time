# 🕒 Daily Date-Time

""" A beginner-friendly Python script that displays the current date, time, and a context-aware greeting. """

# ----------- Overview -----------

# This script prints:
# 📅 Current date
# 🕒 Current time
# 👋 A greeting based on your time:
#   - ☀️ Good Morning (before 12 PM)
#   - 🌤️ Good Afternoon (12 PM – 5 PM)
#   - 🌙 Good Evening (after 5 PM)

# ----------- Sample Output -----------

# 📅 Date: Tuesday, 02 July 2025
# 🕒 Time: 10:23:45 AM
# 👋 Good Morning ☀️

# ----------- How to Use -----------

# 1. Clone the repository:
# git clone https://github.com/Daud-Nisar/daily-date-time.git
# cd daily-date-time

# 2. Run the script:
# python main.py

# ----------- Code (main.py) -----------

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

# ----------- Future Improvements -----------

# - Add GUI using Tkinter
# - Save output to a .txt file
# - Auto-push time daily to GitHub using GitHub Actions
# - Add support for other timezones

# ----------- About Me -----------

# Daud Nisar — Python Developer from Pakistan 🇵🇰
# 💼 Specializing in:
#   - Python Scripts & Automation
#   - Web Scraping
#   - QA Testing with Selenium

# ----------- Connect with Me -----------

# 💻 GitHub: https://github.com/Daud-Nisar
# 💼 LinkedIn: https://www.linkedin.com/in/daud-nisar-aa88a9222/
# 🧰 Upwork: https://www.upwork.com/freelancers/~0152296150762df3c8?mp_source=share

# ----------- Support -----------

# ⭐️ Star this repository
# ✅ Follow me on GitHub
# 💬 Share your feedback or suggest improvements

# 📅 Built with 💖 in Pakistan
