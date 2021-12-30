
IF DB_ID('imporfrut19_21') IS NULL
	CREATE DATABASE imporfrut19_21
USE imporfrut19_21;

IF OBJECT_ID ('CLIENTE') IS NULL 
	CREATE TABLE CLIENTE (
	id_cliente nvarchar(200) primary key not null,
	nombre nvarchar(200),
	telefono int,
	email nvarchar(200),
	tipo_facturacion nvarchar(200),
	id_plaza int
	);
IF OBJECT_ID ('PLAZA') IS NULL 
	CREATE TABLE PLAZA (
	id_plaza int primary key not null,
	id_cliente int not null,
	id_vendedor int
	);
IF OBJECT_ID ('VENDEDOR') IS NULL 
	CREATE TABLE VENDEDOR (
	id_vendedor int primary key not null,
	nombre nvarchar(200), 
	id_plaza nvarchar(200) 
	);
IF OBJECT_ID ('ENTREGAS') IS NULL 
	create table ENTREGAS (
	id_entregas nvarchar(200) not null primary key,
	id_pedido nvarchar(200),
	id_vendedor int,
	id_cliente nvarchar(200),
	fecha_entrega nvarchar(200),
	id_producto int,
	cantidad nvarchar(200)
	);
IF OBJECT_ID ('PRODUCTO') IS NULL
	create table PRODUCTO (
	id_producto int primary key not null ,
	nombre nvarchar(200) not null,
	);
	
IF OBJECT_ID ('DEVOLUCIONES') IS NULL
	create table DEVOLUCIONES	(
	id_devoluciones nvarchar(200) not null primary key,
	id_entregas nvarchar(200),
	fecha_devolucion nvarchar(200)
	);
--ALTER TABLE CLIENTE 
	--ADD FOREIGN KEY (ID_PLAZA) references PLAZA (ID_PLAZA)

--ALTER TABLE VENDEDOR
	--ADD FOREIGN KEY (ID_PLAZA) references PLAZA (ID_PLAZA)

--ALTER TABLE PLAZA 
	--ADD FOREIGN KEY (ID_CLIENTE) references CLIENTE (ID_CLIENTE)

--ALTER TABLE PLAZA
	--ADD FOREIGN KEY (ID_VENDEDOR) references VENDEDOR (ID_VENDEDOR)
	

	
	
--IF OBJECT_ID ('PEDIDO') IS NULL
--	create table PEDIDO (
--	ID_PEDIDO  nvarchar(200) primary key not null,
--	ID_CLIENTE nvarchar(200) not null,    --FK
--	ID_VENDEDOR int not null, --FK
--	ID_PRODUCTO int not null, --FK
--	);

	
