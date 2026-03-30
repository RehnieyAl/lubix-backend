import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config import config

GMAIL_USERNAME = config.GMAIL_USERNAME
GMAIL_PASSWORD = config.GMAIL_APP_PASSWORD


def send_email(to_email: str, subject: str, body: str):
    msg = MIMEMultipart()
    msg['From'] = GMAIL_USERNAME
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USERNAME, GMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Correo enviado exitosamente")
    except Exception as e:
        print(f"Error al enviar correo: {e}")



def send_code_email(to_email: str, code: str, code_type: str):
    
    custom_subject = {
        "verifyEmail": "Código de verificación",
        "resetPassword": "Código para restablecer la contraseña"
    }

    custom_message = {
        "verifyEmail": "Tu código de verificación es: ",
        "resetPassword": "Tu código para restablecer la contraseña es: "
    }

    for i in custom_subject:
        if i == code_type:
            subject = custom_subject[i]
            break
    else:
        ValueError("Tipo de código inválido")

    for i in custom_message:
        if i == code_type:
            body = f"{custom_message[i]} {code}"
            break
    else:
        ValueError("Tipo de código inválido")

    exit_code = send_email(to_email, subject, body)

    if exit_code:
        return code
    return None


