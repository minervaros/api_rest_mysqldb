create database if not exists api_mysql;

use api_mysql;

create table if not exists users(
	id int unsigned not null auto_increment primary key,
    nombre varchar(20) not null,
    edad int not null,
    ciudad varchar(50) not null,
    correo varchar(100) not null
)