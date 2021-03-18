# Creación De un pagina web con Flask

1.  Creación Carpeta
2. Instalar flask y flask-mysql comando

```
pip install flask  
pip install flask-mysqldb
```
3. Crear el archivo principal con la siguiente configuración y especificaciones
```

```

4. Crear la base de datos utilizando el siguiente query;

```sql
show databases;
create database if not exists FLASKTUTORIAL;


use FLASKTUTORIAL;
create table if not exists contacto(
	 id int not null  primary key auto_increment,
	 nombre varchar(255) not null, 
     phone varchar(8) not null default '00000000',
     email varchar(100) not null
);
DESCRIBE contacto;
```

5. 
    