from flask import Flask, render_template, request, redirect, url_for, flash #importar flask, el render_template es para renderizar una plantilla de html y el request para las peticiones
#redirect redirecciona a otra ruta y el url_for es para darle la ruta, flash sirve para mandar mensajes entre vistas
from flask_mysqldb import MySQL #libreria para conectar ala base de datos

app = Flask(__name__) #crear objeto el parametro __name__ es obligatorio

###configuracion base de datos
app.config['MYSQL_HOST'] = 'localhost'  #host donde se encuentra la base de datos
app.config['MYSQL_USER'] = 'root'  #usuario de la base de datos
app.config['MYSQL_PASSWORD'] = 'Inge171819' #contraseña de la base de datos
app.config['MYSQL_DB'] = 'FLASKTUTORIAL' #nombre de la base de datos
mysql = MySQL(app)#instanciar objeto de mysql

#settings
app.secret_key = 'mysecretkey' #esto es para decirle como va a ir protegida nuestra sesion

@app.route('/')#esto es para que cada vez que se entre a la ruta principal se devuelva algo, en este caso la funcion de abajo
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacto')
    data = cur.fetchall()
    print(data)
    return render_template('index.html', contacts = data)#no necesita el nombre de la carpeta, es para renderizar el nombre del archivo

@app.route('/add_contact', methods=['POST'])#de esta manera se agregan las rutas y abajo las funciones para indicar que hacer y retornar
def add_contact():
    if request.method == 'POST': #si me estas tratando de enviar a esta ruta por el metodo POST voy a tratar de hacer algo 
        name = request.form['fullname'] #el reques.fomr['nombreatributo'] devuelve el valor del input con ese nombre asi para los demas
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()#obtiene un cursos de mysql y devuelve un valor a guardar y este permite ejecutar las consulta sql
        cur.execute('INSERT INTO CONTACTO (nombre, phone, email) VALUES (%s, %s, %s)', (name, phone, email)) #esto es para escribir el query
        mysql.connection.commit() #con este comando se ejecuta la consulta escrita
        flash('Contacto agregado satisfactoriamente')
        return redirect(url_for('Index'))
    

@app.route('/edit/<id>')
def edit_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacto WHERE id = {0}'.format(id))
    data = cur.fetchall()
    return render_template('edit_contact.html', contact= data[0])


@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        name = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('''UPDATE CONTACTO SET nombre = %s, phone = %s, email=%s  WHERE id=%s''', (name, phone, email,id))
        mysql.connection.commit()
        flash('Contact Updated Successfully')
        return redirect(url_for('Index'))


@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacto WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('Index'))

if __name__ == '__main__':# validar que se ejecute el archivo principal
    app.run(port = 3000, debug=True)#iniciar el servidor, se especifica el puerto y el debug true es para que se actulice el servidor si se hacen cambios

