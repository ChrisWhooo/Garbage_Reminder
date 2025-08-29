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



