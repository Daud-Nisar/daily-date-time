from datetime import datetime
from zoneinfo import ZoneInfo

# Pakistan Standard Time
now = datetime.now(ZoneInfo("Asia/Karachi"))

# Format date and time
current_time = now.strftime("%I:%M:%S %p")
current_date = now.strftime("%A, %d %B %Y")

# Greeting based on Pakistan time
hour = now.hour

if hour < 12:
    greeting = "Good Morning ☀️"
elif hour < 17:
    greeting = "Good Afternoon 🌤️"
else:
    greeting = "Good Evening 🌙"

# Output
print("📅 Date:", current_date)
print("🕒 Time:", current_time)
print("👋", greeting)
