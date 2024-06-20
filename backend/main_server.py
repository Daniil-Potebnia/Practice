from flask import Flask, render_template, redirect
from flask_login import LoginManager, current_user
from flask_socketio import SocketIO

from orm.db_session import global_init, create_session
from orm.user import User

app = Flask(__name__, template_folder='../frontend/templates')
app.config['SECRET_KEY'] = 'dahre-project'

login_manager = LoginManager()
login_manager.init_app(app)

socketio = SocketIO(app)


def login_required(func):
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect('/register')
        return func(*args, *kwargs)
    return wrapper


@login_manager.user_loader
def load_user(user_id):
    db_sess = create_session()
    return db_sess.query(User).get(user_id)


@app.route('/', methods=['GET'])
def main_page():
    return render_template('main_page.html', title='Начало')


@app.route('/u')
def a():
    with create_session() as session:
        print(session.query(User).all())
    return ''


if __name__ == '__main__':
    global_init()
    socketio.run(app=app, host='127.0.0.1', port=8080, allow_unsafe_werkzeug=True)
