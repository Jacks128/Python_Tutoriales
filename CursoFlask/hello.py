from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s' % name

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' %guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest = name))

@app.route('/hi')
def hi():
    str = """
        <h1>HI WORLD </h1>
    """
    return str

@app.route('/render/hi')
def renderHi():
    return render_template('hi.html')

@app.route('/static')
def staticf():
    return render_template('static.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        user=request.form['name']
        return redirect(url_for('hello_guest', guest=user ))
    else:
        user = request.args.get('name')
        return redirect(url_for('hello_guest', guest=user))


#app dat
@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        print(result)
        return render_template('result.html', result = result)
app.run(debug=True)