# # Send e-mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Send e-mail of the list
def enviaremail(fromaddr,toaddr,search):
    try:
        #fromaddr = "deko123456789@hotmail.com"
        #toaddr = "castrodeko11@bol.com.br"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        cc = ['castrodeko11@bol.com.br']
        msg['Subject'] = "SAP Softtek"
        body = '''Bom dia Prezado (a),

Sou André da área de sistemas aplicações e estou cuidando da pesquisa de satisfação do nosso parceiro de SAP(Softtek),
recentemente foi fechado um chamado em seu nome
você poderia responder a pesquisa ? 

''' \
+ \
search \
+'''

Não leva mais que 2 minutos.

Obrigado.

André Oliveira
Sistemas – Aplicações
Logicalis


        '''
        msg.attach(MIMEText(body, 'plain'))
        s = smtplib.SMTP('smtp.live.com',587)
        s.starttls()
        s.login(fromaddr, "familia123456789")
        text = msg.as_string()
        toaddrs = [toaddr] + cc
        s.sendmail(fromaddr, toaddrs, text)
        print("E-mail enviado com sucesso")
        s.quit()
    except:
        print("Erro ao enviar e-mail")





