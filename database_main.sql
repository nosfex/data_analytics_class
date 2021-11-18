
IF DB_ID('imporfrut19_21') IS NULL
	CREATE DATABASE imporfrut19_21
USE imporfrut19_21;

IF OBJECT_ID ('CLIENTE') IS NULL 
	CREATE TABLE CLIENTE (
	ID_CLIENTE nvarchar(200) primary key not null,
	NOMBRE nvarchar(200),
	TELEFONO int,
	EMAIL nvarchar(200),
	TIPO_FACTURACION nvarchar(200),
	ID_PLAZA int
	);
IF OBJECT_ID ('PLAZA') IS NULL 
	CREATE TABLE PLAZA (
	ID_PLAZA int primary key not null,
	ID_CLIENTE nvarchar(200),
	ID_VENDEDOR int
	);
IF OBJECT_ID ('VENDEDOR') IS NULL 
	CREATE TABLE VENDEDOR (
	ID_VENDEDOR int primary key not null,
	NOMBRE nvarchar(200), 
	ID_PLAZA nvarchar(200) 
	);
	IF OBJECT_ID ('entregas') IS NULL 
	create table entregas (
	id_entregas nvarchar(200) not null primary key,
	id_pedido nvarchar(200),
	fecha_entrega datetime,
	id_producto nvarchar(300),
	cantidad nvarchar(200)
	);
	IF OBJECT_ID ('devoluciones') IS NULL
	create table devoluciones	(
	id_devoluciones int not null primary key,
	id_entregas int,
	fecha_devolucion datetime
	);
--ALTER TABLE CLIENTE 
	--ADD FOREIGN KEY (ID_PLAZA) references PLAZA (ID_PLAZA)

--ALTER TABLE VENDEDOR
	--ADD FOREIGN KEY (ID_PLAZA) references PLAZA (ID_PLAZA)

--ALTER TABLE PLAZA 
	--ADD FOREIGN KEY (ID_CLIENTE) references CLIENTE (ID_CLIENTE)

--ALTER TABLE PLAZA
	--ADD FOREIGN KEY (ID_VENDEDOR) references VENDEDOR (ID_VENDEDOR)
