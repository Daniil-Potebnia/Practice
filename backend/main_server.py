from waitress import serve
from flask import Flask, render_template, redirect, request
from flask_login import LoginManager, current_user, login_user, logout_user
from flask_socketio import SocketIO

from orm.db_session import global_init, create_session
from orm.user import User

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
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
    return render_template('main_page.html', title='Главная страница')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        form = request.form.to_dict()
        with create_session() as session:
            valid_login = not len(session.query(User).filter(User.login == form['login']).all())
            valid_email = not len(session.query(User).filter(User.email == form['email']).all())
        if valid_login and valid_email:
            with create_session() as session:
                new_user = User()
                new_user.set_email(form['email'])
                new_user.set_login(form['login'])
                new_user.set_hashed_password(form['password'])
                session.add(new_user)
                session.commit()
                login_user(new_user)
            return redirect('/')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form = request.form.to_dict()
        with create_session() as session:
            user = session.query(User).filter(User.login == form['login']).first()
            if user.check_hashed_password(form['password']):
                login_user(user)
            else:
                return render_template('login.html')
        return redirect('/')


@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


if __name__ == '__main__':
    global_init()
    socketio.run(app=app, host='127.0.0.1', port=8080, allow_unsafe_werkzeug=True, debug=True)
    # serve(app, host='127.0.0.1', port=8080)
