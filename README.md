# Garbage_Reminder

A simple Python-based reminder bot that sends scheduled email notifications about local garbage collection.

## 📌 Features

- ⏰ Daily reminder at 20:00 (Japan time)
- 📩 Sends email using SMTP
- 📅 Customizable garbage collection schedule
- 📨 HTML email content with template
- 🔄 Automatically runs as a background service using `apscheduler`

---

## 🧠 How It Works

This script checks the garbage collection schedule and sends a reminder email the evening **before** a scheduled pickup.

- Schedule is defined in `GARBAGE_SCHEDULE`
- Email content is rendered from `garbage_template.html`
- Scheduler runs daily using `apscheduler`

---

## 🚀 Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/ChrisWhooo/Garbage_Reminder.git
cd Garbage_Reminder
```
2. Install python dependencies
```bash
pip install -r requirements.txt
```
3. Set your mail inside the script
```bash
SENDER_EMAIL = "your@email.com"
RECEIVER_EMAILS = ["target1@example.com", "target2@example.com"]
SMTP_SERVER = "your.smtp.server"
SMTP_PORT = 25
```
4. Customise your garbage schedule
```bash
GARBAGE_SCHEDULE = {
    "Sunday": "資源ごみ",
    "Tuesday": "燃えるゴミ",
    "Thursday": "プラスチック",
    "Friday": "燃えるゴミ"
}
```
5. Run the script
```bash
python3 auto_reminder.py
```
🧪 Test It Immediately
```bash
python3 auto_reminder.py test
```
## 📁 Project Structure
```bash
Garbage_Reminder/
├── auto_reminder.py         # Main script
├── garbage_template.html    # Email HTML template
├── requirements.txt         # Python dependencies
└── README.md     
```
