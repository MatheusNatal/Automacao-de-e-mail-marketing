import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import datetime
import time

# Defina a hora em que deseja que a ação ocorra
hora_desejada = datetime.time(12, 30) # 12:30 PM

while True:
    # Obtenha a hora atual
    hora_atual = datetime.datetime.now().time

    # Verifique se a hora atual é igual à hora desejada
    if hora_atual == hora_desejada:

        # Configuração do servidor SMTP e informações da conta
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login("seu_email@gmail.com", "sua_senha")

        # Criação da mensagem
        msg = MIMEMultipart()
        msg['From'] = "seu_email@gmail.com"
        msg['To'] = "destinatario@example.com"
        msg['Subject'] = "Assunto do E-mail"

        # Adicionando o corpo da mensagem
        corpo = MIMEText("Corpo do E-mail")
        msg.attach(corpo)

        # Adicionando uma imagem ao e-mail
        with open("imagem.jpg", "rb") as f:
            imagem = MIMEImage(f.read())
            msg.attach(imagem)

        # Enviando a mensagem
        server.sendmail("seu_email@gmail.com", "destinatario@example.com", msg.as_string())
        server.quit()

        # Espere 24 horas antes de executar a ação novamente
        time.sleep(24 * 60 * 60) # 24 horas em segundos