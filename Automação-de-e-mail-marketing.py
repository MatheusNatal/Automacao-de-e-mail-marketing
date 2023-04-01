import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Configurações do servidor SMTP e informações da conta de e-mail
smtp_server = 'smtp.office365.com'
smtp_port = 587
smtp_username = 'carloshenrique783@hotmail.com'
smtp_password = 'Pimenta10@'

# Informações sobre o remetente do e-mail
de = 'carloshenrique783@hotmail.com'

# Ler lista de destinatários a partir do arquivo lista.txt
with open('lista.txt', 'r') as f:
    para_lista = [linha.strip() for linha in f]

# Crie uma mensagem de e-mail com corpo HTML
msg = MIMEMultipart('related')
msg['From'] = de
msg['Subject'] = "OPORTUNIDADE ÚNICA"

html = """\
<html>
  <body>
    <p>Olá, <br>

Você sabia que é possível ganhar dinheiro na internet sem sair de casa? Se você está procurando uma maneira de aumentar sua renda ou deseja criar uma nova fonte de renda, temos a solução perfeita para você.<br>
<br>
Nosso curso de marketing digital é uma oportunidade incrível para aprender as estratégias mais eficazes para ganhar dinheiro online. Com a orientação de nossos especialistas em marketing, você aprenderá como criar e promover produtos digitais, como usar o marketing de afiliados e muito mais.<br>
<br>
Além disso, você terá acesso a aulas práticas e exercícios para aplicar todo o conhecimento que aprendeu. E se surgirem dúvidas, nossos tutores estarão disponíveis para ajudar.<br>
<br>
Não perca a chance de transformar seu futuro financeiro. Inscreva-se agora em nosso curso de marketing digital e comece a ganhar dinheiro na internet.<br>
<br>
Atenciosamente,<br>
Carlos Henrique, Gestor de vendas empresa piru.</p>
    <p><a href="https://metodohomeofficelucrativo.com.br/pv/?mcr=AQM22263687">Clique aqui</a>e mude de vida agora mesmo!</p>
  </body>
</html>
"""

# Função para enviar o e-mail
def enviar_email():
    for para in para_lista:
        # Crie um novo objeto MIMEMultipart para cada destinatário
        msg_individual = MIMEMultipart()
        msg_individual['To'] = para
        msg_individual['Subject'] = 'Oportunidade Única'
        msg_individual.attach(MIMEText(html, 'html'))
        '''msg_individual.attach(img)'''

        # Conecte-se ao servidor SMTP e envie o e-mail
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.sendmail(de, para, msg_individual.as_string())
        smtp.quit()
        print(f'E-mail enviado com sucesso para {para}!')

# Agende o envio do e-mail para as 10:30 todos os dias
schedule.every().day.at("10:06").do(enviar_email)

# Loop principal para executar as tarefas agendadas
while True:
    schedule.run_pending()
    time.sleep(1)