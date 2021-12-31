
# Version 0.1 Documentacion Grupo Coderhouse 18890

## Cambios Realizados a Base de Datos:
- Actualizacion Script python para generacion y parseo de datos
- Base de datos cambiada a csv_export_0_1.csv
- Script soporta upload a server de Azure
- Soporte de set como data type por razones de performance
- Buscando como mejorar la query para cambiar de "INSERT INTO" a un "INSERT INTO MANY / INSERT ARRAY" para optimizacion
- Cambios a operacion de commit. Se removio el commit entre inserts into para un unico commit por razones de performance

## Cambios Realziados a .pbix:
- Version Actual pbix: project_pbi3.pbix
- Base de datos es tomada desde Azure SQL.
- Se cambio referencia de bases de datos desde TABLE_Ledger a TABLE normal. Se usaba incorrectamente Ledger lo cual causaba issues de performance
- Se agregaron Measures Relacionadas a tipo de producto:
	- Product1001
	- Product1002
	- Product1004
	- Product2001
	- Product2003
	- Product7001
	- Product7002
	- Product7003
	- Product7004
	- Product7007
- Se agregaron Measures relacionadas a Pedidos y ventas:
	- TotalPedidos
	- TotalPedidosDevueltos
- Se agregaron Listas de Cliente, Pedido, Producto:
	- ListIDCliente
	- ListIDPedido
	- ListIDProducto
- Se agregaron Ventas por vendedor:
	- VentasDeliana
	- VentasEtc ....
- Se agregaron measures con variable Simple:
	- YearRangeSales
- Se agregaron measures con mas de una variable:
	- PorcentajePromocion1001
	- PorcentajePromocion1002
	- PorcentajePromocion1004
	- DevolucionesPlatanos
- Se cambiaron tipos de datos. Datos se habian simplificado anteriormente por razones de automatizacion:
	- Table EntregaS:
		- cantidad -> string to int
		- id_producto -> string to int
		- fecha_entrega -> string to date
- Se crearon Dashboards para representacion grafica
	- Dos Paginas de dashboard nombradas KPI2 / KPI2-1
	- Tabla 1 contiene informacion de ventas que contiene datos de 2019 a 2021
	- Tabla 2 contiene informacion de devolucion de ventas de 2019 a 2021
	- Filtros agregados por producto y fecha 
	- Se agrego lista de ventas por cliente
	- Se agregaron graficos de devolucion
	- Se agregaron graficos de venta por producto y cantidades de venta por vendedor