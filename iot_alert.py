import random
import time
import smtplib
from email.mime.text import MIMEText

SEUIL_TEMP = 30
SEUIL_MOTION = 1
ALERT_INTERVAL = 10

SENDER_EMAIL = "meminsidi2@gmail.com"
RECIPIENT_EMAIL = "M2lemine.sd@gmail.com"
EMAIL_PASSWORD = "pglg ndme qydb qayc"

last_alert_time = 0

def send_email_alert(value, type_alert):
    msg = MIMEText(f"Alerte : {type_alert} a dépassé le seuil ! Valeur : {value}")
    msg['Subject'] = "IoT Alert"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print(f"Email envoyé pour {type_alert}")
    except Exception as e:
        print(f"Erreur en envoyant l'email : {e}")

def get_temperature():
    return random.randint(20, 40)

def get_motion():
    return random.choice([0, 1])

while True:
    temp = get_temperature()
    motion = get_motion()
    print(f"Température: {temp}°C, Mouvement: {motion}")

    current_time = time.time()

    if temp > SEUIL_TEMP:
        print("Température dépassée !")
        if current_time - last_alert_time > ALERT_INTERVAL:
            send_email_alert(temp, "Température")
            last_alert_time = current_time

    if motion >= SEUIL_MOTION:
        print("Mouvement détecté !")
        if current_time - last_alert_time > ALERT_INTERVAL:
            send_email_alert(motion, "Mouvement")
            last_alert_time = current_time

    time.sleep(2)
