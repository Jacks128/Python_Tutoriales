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