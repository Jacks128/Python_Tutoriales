import yagmail
correo = yagmail.SMTP('car123che@gmail.com', 'ingenieria20')
correo.send(to='Carlosngv99@hotmail.com', subject='Prueba', contents='Rola TEO PTM')
#https://myaccount.google.com/lesssecureapps
#Para que funcione la libreria, tu correo, el correo que envia el mensaje debe ser gmail
#debes tener una cuenta gmail, luego ingresar al link de la linea 4 y darle si en permitir
#es para que permita a un dispositivo desconocido enviar el correo

#https://support.google.com/a/answer/2956491#sendinglimitsforrelay
#este otro link de la linea 9 es para ver el limite de correos que puedes mandar y otras descripciones

#########################################INSTALAR LIBRERIA EN LA COMPUTADAORA DE PRIMERO#############################################
#pip install yagmail
#pip3 install yagmail
#sudo pip3 install yagmail
#sudo pip install yagmail

#usar los primeros dos comando para instalar la libreria en windows, probar cual funciona, y los ultimos 2 es para instalar en ubuntu
#si luego de instalar no se reconoce el paquete reiniciar la PC