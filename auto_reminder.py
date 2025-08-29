import smtplib
import datetime
from email.mime.text import MIMEText
from email.header import Header
import os
from apscheduler.schedulers.blocking import BlockingScheduler

SMTP_SERVER = "localhost"
SMTP_PORT = 25
SENDER_EMAIL = "wuhan6582@gmail.com"
RECEIVER_EMAILS = ["wuhan6582@gmail.com","chriscavendish01@gmail.com"]

GARBAGE_SCHEDULE = {
    "Sunday": "資源ごみ",
    "Tuesday": "燃えるゴミ",
    "Thursday": "プラスチック",
    "Friday": "燃えるゴミ"
}

def generate_html(garbage_type):
    """ Read HTML template and fill in data """
    now = datetime.datetime.now()
    tomorrow = datetime.datetime.now()+datetime.timedelta(days=1)
    weekday_name = tomorrow.strftime('%A')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, "garbage_template.html")

    try:
        with open(template_path, "r", encoding="utf-8") as f:
            html = f.read()
            print(f"[{now}] HTML template loaded.")
    except FileNotFoundError:
        print(f"[{now}] HTML template file not found: {template_path}")
        html = "<html><body><h3>{{subject}}</h3><p>Garbage Type: {{garbage_type}}</p><p>Date: {{date}}</p></body></html>"

    return html.replace("{{subject}}", "Garbage Collection Reminder") \
        .replace("{{garbage_type}}", garbage_type) \
        .replace("{{date}}", weekday_name)

def send_html_email(subject, content):
    """ Send an HTML email """
    print(f"[{datetime.datetime.now()}] Preparing to send email:")
    print(f"Subject: {subject}")
    print(f"Recipients: {RECEIVER_EMAILS}")
    try:
        msg = MIMEText(content, 'html', 'utf-8')
        msg['From'] = f'"Garbage Collection Reminder Bot" <{SENDER_EMAIL}>'
        msg['To'] = ", ".join(RECEIVER_EMAILS)
        msg['Subject'] = Header(subject, 'utf-8')

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAILS, msg.as_string())
        
        print(f"[{datetime.datetime.now()}]  Email sent successfully!")
    except Exception as e:
        print(f"[{datetime.datetime.now()}]  Failed to send email: {e}")

def garbage_reminder():
    """ Check the garbage schedule and send reminders """
    today = datetime.datetime.now().strftime("%A")
    print(f"[{datetime.datetime.now()}]  Today is: {today}")
    if today in GARBAGE_SCHEDULE:
        garbage_type = GARBAGE_SCHEDULE[today]
        print(f"[{datetime.datetime.now()}]  Garbage type for today: {garbage_type}")
        content = generate_html(garbage_type)
        send_html_email(f" Garbage Collection Reminder - {garbage_type}", content)
    else:
        print(f"[{datetime.datetime.now()}]  No garbage collection scheduled for today.")

# Scheduled job
scheduler = BlockingScheduler(timezone='Asia/Tokyo')
scheduler.add_job(garbage_reminder, 'cron', hour=20, minute=0)  # Remind at 8 PM daily

if __name__ == "__main__":
    print(f"[{datetime.datetime.now()}] Garbage collection reminder service started.")
    # === TEST ONLY ===
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
        weekday_name = tomorrow.strftime('%A')
        today = datetime.datetime.now().strftime('%A')
        if today in GARBAGE_SCHEDULE:
            garbage_type = GARBAGE_SCHEDULE[today]
            content = generate_html(garbage_type)
            send_html_email(f"[TEST] Garbage Reminder - {garbage_type}", content)
        else:
            print(f"[{datetime.datetime.now()}] No garbage scheduled for tomorrow ({weekday_name}).")
        sys.exit(0)
    # === END TEST ===

    scheduler.start()

