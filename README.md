# Automatização de Emails

## Saiba como um servidor SMTP funciona
O funcionamento de um servidor SMTP é bem simples de entender. Quando uma pessoa escreve um email e clica em *enviar*, todas as informações referentes a ele são enviadas para o servidor SMTP.

Nesse momento, o **servidor** vai adequar o conteúdo recebido aos padrões do protocolo de transferência de email e encaminhá-lo para a internet, onde será transmitido: similar ao que os carteiros fazem ao recolher as correspondências a serem enviadas.

Eles fazem a organização conforme os destinos e identificam os pacotes conforme as regras internas da companhia. Então, os malotes são levados para transporte, até o próximo ponto de controle, que será a agência responsável por fazer a entrega final.

No caso dos emails, esse papel é realizado por um servidor **POP/IMAP**, que pega as mensagens recebidas na internet e as leva até as caixas dos destinatários. Exatamente como fazem os carteiros todos os dias pelas ruas, porém de forma digital e em poucos segundos.

## Informações específicas dos principais servidores gratuitos
### Lista de servidores e portas SMTP:
1. Gmail
    * servidor SMTP: smtp.gmail.com;
    * porta de saída: 465, caso esteja usando SSL ou 587 se for TLS.

1. Hotmail
    * servidor SMTP: smtp.live.com;
    * porta de saída: 25 ou 465.

1. Yahoo
    * servidor SMTP: smtp.mail.yahoo.com;
    * porta de saída: 465.

1. Outlook.com
    * servidor SMTP: SMTP.office365.com;
    * porta de saída: 587.


## Capacidade de envio
Nos servidores gratuitos, tais como Gmail, Yahoo e Outlook, o limite diário de envios é baixo, girando em torno de 100 mensagens. Para quem não utiliza esse canal para envio de email marketing, é uma quantidade bastante razoável.

Já nas plataformas pagas, o limite varia conforme o plano e a empresa, mas, de toda forma, são quantidades maiores, específicas para quem faz um uso mais massivo. Se a sua base de clientes é grande e você deseja fazer envios de campanhas, os serviços pagos são mais indicados.

> https://rockcontent.com/br/blog/servidor-smtp/


# Configurando o código:

## Definindo a hora: 

    'hora_desejada = datetime.time(12, 30) # 12:30'
        * Utilizando-se o formato 24 horas, defina o horario de envio da mensagem.
    
    Exemplo:

        hora(s) | Minuto(s)
        :---: | :---:
        12 | 30
        18 | 45
        23| 59
        09 | 43

## Configuração do servidor SMTP e informações da conta:

    '''server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login("seu_email@gmail.com", "sua_senha")'''
---
    'server = smtplib.SMTP('smtp.office365.com', 587)'
        * Defina o servidor SMTP e a respectiva porta que ***você*** utiliza, no exemplo acima temos para uma conta Outlook.com
---
    'server.login("seu_email@gmail.com", "sua_senha")'
        * Neste campo você deverá informar seu email e senha do e-mail que você utiliza, para que o programa consiga enviar as mensagens.

## Criação da mensagem:
    '''msg = MIMEMultipart()
       msg['From'] = "seu_email@gmail.com"
       msg['To'] = "destinatario@example.com"
       msg['Subject'] = "Assunto do E-mail"'''

* Nesse campo você deverá informar o seu e-mail, o e-mail destinatário e o assunto do conteúdo.

## Adicionando o corpo da mensagem
     '''corpo = MIMEText("Corpo do E-mail")
        msg.attach(corpo)'''
---
    'corpo = MIMEText("Corpo do E-mail")'
        * Neste campo você deverá escrever todo o conteúdo do e-mail.

## Adicionando uma imagem ao e-mail
    '''with open("imagem.jpg", "rb") as f:
            imagem = MIMEImage(f.read())
            msg.attach(imagem)'''
---
    'with open("imagem.jpg", "rb") as f:'
        * Neste campo você deverá informar o nome exato da imagem que deseja enviar e a mesma deve estar dentro da pasta do código.

## Enviando a mensagem
        '''server.sendmail("seu_email@gmail.com", "destinatario@example.com", msg.as_string())
        server.quit()'''
---
    'server.sendmail("seu_email@gmail.com", "destinatario@example.com", msg.as_string())'
        *Neste campo você deverá informar o seu e-mail e o e-mail do destinatário.

# Feito tudo isso, você pode rodar o código.

