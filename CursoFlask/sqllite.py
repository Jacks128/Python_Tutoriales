from flask import Flask, render_template ,request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/enternew')
def new_student():
    return render_template('student2.html')

@app.route('/addrec' , methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr= request.form['add']
            city = request.form['city']
            pin = request.form['pin']
            with sql.connect('./sqliteDB/test.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO STUDENT VALUES (?,?,?,?)", (nm, addr, city, pin) )
                con.commit()
                msg = "Record succesfully added"
        except:
            con.rollback()
            msg = "error in insert op"
        finally:
            return render_template("result2.html", msg=msg)
            con.close()

@app.route('/list')
def list():
    con = sql.connect('./sqliteDB/test.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from student")
    rows = cur.fetchall()
    return render_template("list.html", rows = rows)

app.run(debug=True)