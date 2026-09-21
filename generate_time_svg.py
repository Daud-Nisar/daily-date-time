from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path
import html

# Pakistan Standard Time
now = datetime.now(ZoneInfo("Asia/Karachi"))

current_time = now.strftime("%I:%M:%S %p")
current_date = now.strftime("%A, %d %B %Y")

hour = now.hour

if hour < 12:
    greeting = "Good Morning ☀"
elif hour < 17:
    greeting = "Good Afternoon 🌤"
else:
    greeting = "Good Evening 🌙"

svg = f'''<svg width="700" height="180" viewBox="0 0 700 180"
xmlns="http://www.w3.org/2000/svg">

<rect width="700" height="180" rx="20" fill="#0d1117"/>

<text x="350" y="55"
      text-anchor="middle"
      font-family="Arial, sans-serif"
      font-size="22"
      fill="#8b949e">
    Pakistan Standard Time • PKT
</text>

<text x="350" y="105"
      text-anchor="middle"
      font-family="monospace"
      font-size="42"
      font-weight="bold"
      fill="#58a6ff">
    {html.escape(current_time)}
</text>

<text x="350" y="140"
      text-anchor="middle"
      font-family="Arial, sans-serif"
      font-size="17"
      fill="#c9d1d9">
    {html.escape(current_date)}
</text>

<text x="350" y="165"
      text-anchor="middle"
      font-family="Arial, sans-serif"
      font-size="14"
      fill="#8b949e">
    {html.escape(greeting)}
</text>

</svg>
'''

output = Path(".github/assets/pkt-time.svg")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(svg, encoding="utf-8")

print(f"Updated Pakistan time: {current_time}")
