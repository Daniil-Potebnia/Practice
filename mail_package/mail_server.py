from waitress import serve
from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dahre-project'
app.config['MAIL_SERVER'] = 'smtp.yandex.ru'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'Dahre123@yandex.ru'
app.config['MAIL_DEFAULT_SENDER'] = 'Dahre123@yandex.ru'
app.config['MAIL_PASSWORD'] = 'hkaqyggxzrymtfuv'
mail = Mail(app)


@app.route('/check_email/<email>', methods=['GET'])
def check_email(email):
    msg = Message("Подтверждение почты", recipients=[email])
    msg.html = render_template('mail_confirm.html')
    return ''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1000, debug=True)
    # serve(app, host='127.0.0.1', port=1000)
