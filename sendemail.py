import smtplib

fromaddr = 'gaster300@gmail.com'

toaddr  = 'kamolwilliams@gmail.com'

message = """From: {} <{}>

To: {} <{}>

Subject: {}

{}""" messagetosend = message.format(

                             fromname,

                             fromaddr,

                             toname,

                             toaddr,

                             subject,

                             msg)

# Credentials (if needed)

username = 'gaster300@gmail.com'

password = 'mynoyvcvcetkbnas'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddrs, messagetosend)

server.quit()