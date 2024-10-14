import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os import environ

def enviar(dados):
    host = 'smtp.umbler.com'
    user = environ.get('email_servicerapide')
    password = environ.get('password_email_servicerapide')
    port = '587'

    servidor = smtplib.SMTP(host=host, port=port)
    servidor.ehlo()
    # servidor.starttls()
    servidor.login(user=user,password=password)

    corpoHTML="<table style='margin-left: auto;margin-right: auto;' >" \
            "<tr>" \
              "<th colspan='2'>" \
              "E-MAIL DE RECUPERACAO DE SENHA."\
            "</th>"\
          "</tr>" \
          "<tr>" \
              "<td>NOME:" \
              "</td>" \
              "<td>"+dados['nome']+"</td>" \
          "</tr>" \
          "<tr>" \
              "<td>CPF:" \
              "</td>" \
              "<td>"+dados['cpf']+"</td>" \
          "</tr>" \
        "<tr>"\
          "<tr>" \
              "<td>DATA DO EXAME:" \
              "</td>" \
              "<td>"+str(dados['data'])+"</td>" \
          "</tr>" \
          "<tr>" \
              "<td>E-MAIL:" \
              "</td>" \
              "<td>"+dados['email']+"</td>" \
          "</tr>" \
          "<tr>" \
              "<td>ESTABELECIMENTO:" \
              "</td>" \
              "<td>"+str(dados['clinica'])+"</td>" \
          "</tr>" \
          "<tr>" \
              "<td>OBSERVAÇÕES:" \
              "</td>" \
              "<td>"+dados['informacoes']+"</td>" \
          "</tr>" \
        "<tr>"\
            "<td colspan='2' style='font-size: xx-small;'>SERVICE RAPIDE TECNOLOGIA."\
                "<br>"\
                "Natal\RN"\
            "</td>"\
          "</tr>"\
      "</table>"

    email = MIMEMultipart()
    email['From'] = environ.get('email_servicerapide')
    email['To'] = environ.get('email_cliente')
    email['Subject'] = 'RECUPERAÇÃO DE PROTOCOLO SERVICE RAPIDE'

    email.attach(MIMEText(corpoHTML, 'html'))

    servidor.sendmail(email['From'],email['To'],email.as_string())

    servidor.quit()
