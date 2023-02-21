import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import schedule
import time


# Configuração do servidor SMTP e informações da conta
def enviar_email():
    with open('emails.txt', 'r') as arquivo:
        lista_emails = arquivo.read().splitlines()

    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login("seu_email@example.com", "sua_senha")

    # Criação da mensagem
    msg = MIMEMultipart()
    msg['From'] = "seu_email@example.com"
    destinatarios = lista_emails
    msg['Subject'] = "Assunto do E-mail"

    # Adicionando o corpo da mensagem
    corpo = MIMEText("Corpo do E-mail")
    msg.attach(corpo)

    # Adicionando uma imagem ao e-mail
    with open("imagem.jpg", "rb") as f:
        imagem = MIMEImage(f.read())
        msg.attach(imagem)

    # Enviando a mensagem
    server.sendmail("seu_email@example.com", ", ".join(destinatarios), msg.as_string())
    server.quit()

# Configurar o agendamento de envio de e-mails
schedule.every().day.at("09:00").do(enviar_email)  # Envio diário às 09:00
schedule.every().day.at("14:30").do(enviar_email)  # Envio diário às 14:30

# Loop principal para executar o agendamento
while True:
    schedule.run_pending()
    time.sleep(60)  # Esperar 1 minuto antes de verificar novamente
