from flask import Flask, redirect, url_for, request, render_template
import hashlib
import db_tools as db
import engine_file as ef
app = Flask(__name__)

u = ef.UserInfo()
db.init_table()


@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template('main_page.html')


@app.route('/hello',  methods=['POST', 'GET'])
def hello_action():
    hello_activity = request.form['what_to_do']
    if hello_activity == 'Generator':
        return redirect(url_for('generator'))
    elif hello_activity == 'Login':
        return redirect(url_for('login'))
    elif hello_activity == 'User_place':
        return redirect(url_for('account_side', username=u.user_name))
    elif hello_activity == 'Else':
        return redirect(url_for('looser'))


@app.route('/login')
def login():
    return render_template('index.html')


@app.route('/check', methods=['POST'])
def ckeck_login():
    user_name = request.form['username']
    passwd = request.form['password']
    u.sing_user(user_name, passwd)
    # passwd_from_db = DB.select_user(user_name)
    # user_passwd = hashlib.sha512(passwd.encode())
    # if user_passwd.hexdigest() == passwd_from_db:
    if user_name == 'a' and passwd == 'a':
        return redirect(url_for('account_side', username=user_name))
    else:
        return redirect(url_for('looser'))


@app.route('/user/<username>')
def account_side(username):
    if u.user_name == 'No_one':
        return redirect(url_for('looser'))
    else:
        return render_template('account_side.html', func=u.user_name)


@app.route('/generator_action', methods=['POST'])
def generator_action():
    q1 = request.form['q1']
    if q1 == '1':
        return render_template('hello.html', func=ef.weak_gen())
    elif q1 == '2':
        return render_template('hello.html', func=ef.strong_gen())
    elif q1 == '3':
        return render_template('hello.html', func=ef.unix_pass_gen())
    elif q1 == '4':
        return redirect(url_for('hello'))


@app.route('/generator', methods=['POST', 'GET'])
def generator():
    return render_template('generator.html')


@app.route('/looser')
def looser():
    return 'Do zobaczenia'

if __name__ == "__main__":
    app.debug = True
