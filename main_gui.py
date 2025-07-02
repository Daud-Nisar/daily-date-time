import tkinter as tk
from datetime import datetime

# Get current time, date, greeting
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

# Save to log.txt (append mode)
with open("log.txt", "a", encoding="utf-8") as file:
    file.write(f"📅 Date: {current_date}\n")
    file.write(f"🕒 Time: {current_time}\n")
    file.write(f"👋 {greeting}\n")
    file.write("-" * 30 + "\n")

# GUI Setup
root = tk.Tk()
root.title("🕒 Daily Date-Time")
root.geometry("400x200")
root.resizable(False, False)

label_font = ("Helvetica", 14)

tk.Label(root, text=f"📅 Date: {current_date}", font=label_font).pack(pady=5)
tk.Label(root, text=f"🕒 Time: {current_time}", font=label_font).pack(pady=5)
tk.Label(root, text=f"👋 {greeting}", font=label_font).pack(pady=10)

root.mainloop()
