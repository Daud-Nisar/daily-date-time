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

with open("log.txt", "a", encoding="utf-8") as file:
    file.write(f"📅 Date: {current_date}\n")
    file.write(f"🕒 Time: {current_time}\n")
    file.write(f"👋 {greeting}\n")
    file.write("-" * 30 + "\n")
