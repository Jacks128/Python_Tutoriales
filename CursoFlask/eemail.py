from flask import Flask
from flask_mail import Mail, Message
app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']= 465
app.config['MAIL_USERNAME']='moveitgt17@gmail.com'
app.config['MAIL_PASSWORD']='ingenieria17'
app.config['MAIL_USE_TLS']= False
app.config['MAIL_USE_SSL']= True
mail = Mail(app)
@app.route('/')
def index():
    msg = Message('Hello', sender="moveitgt17@gmail.com" , recipients=["car123che@gmail.com"])
    msg.body = "HELLO FROM FLASK"
    mail.send(msg)
    return 'MEssage'

app.run(debug=True)