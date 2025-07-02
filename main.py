from datetime import datetime

# Get current date and time
now = datetime.now()

# Format time and date
current_time = now.strftime("%I:%M:%S %p")
current_date = now.strftime("%A, %d %B %Y")

# Greeting based on time
hour = now.hour
if hour < 12:
    greeting = "Good Morning ☀️"
elif 12 <= hour < 17:
    greeting = "Good Afternoon 🌤️"
else:
    greeting = "Good Evening 🌙"

# Output
print("📅 Date:", current_date)
print("🕒 Time:", current_time)
print("👋", greeting)
