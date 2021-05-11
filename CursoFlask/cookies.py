from flask import Flask, render_template, url_for, request, make_response, redirect, flash
app = Flask(__name__)
app.secret_key = 'rangdom string'

@app.route('/')
def index():
    return render_template('setcookie.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setCookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)
        return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome %s </h1>' %name

# lgoin


@app.route('/log')
def log():
    return render_template('login.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST' and request.form['name'] == 'admin':
        return redirect(url_for('success'))
    return redirect(url_for('log'))

@app.route('/succes')
def success():
    return 'login successfully'
#messages
@app.route('/i')
def i():
    return render_template('index.html')

@app.route('/logindos', methods=['GET', 'POST'])
def logindos():
    error = None
    if request.method == 'POST':
        if request.form['user'] != 'admin' or request.form['pass'] != 'admin':
            error = 'Invalid username or password'
        else:
            flash('Your were succesfully login')
            flash('log out before login agian')
            return redirect(url_for('i'))
    return render_template('log_in.html', error=error)

app.run(debug=True)