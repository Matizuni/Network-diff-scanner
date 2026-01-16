import smtplib
from email.mime.text import MIMEText

EMAIL_ENABLED = False   # 🔥 CAMBIA A True CUANDO LO USES

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL_FROM = "matirekor2@gmail.com"
EMAIL_TO = "matirekor2@gmail.com"
EMAIL_PASSWORD = "kofi1231"

def send_email_alert(subject, body):
    if not EMAIL_ENABLED:
        return

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("[*] Alerta enviada por email")
    except Exception as e:
        print(f"[!] Error enviando email: {e}")


