/*Creamos la base de datos*/
CREATE DATABASE shopdb;

/*Creamos la tabla client*/
CREATE TABLE client(
    id_client INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    adreess VARCHAR(100),
    country VARCHAR(50),
    email VARCHAR(50),
    cellphone VARCHAR(12),
    telephone VARCHAR(12),
    job_title VARCHAR(100),
    gender VARCHAR(6),
    college VARCHAR(150)
) PARTITION BY LIST (gender);

/*Creamos la tabla product*/
CREATE TABLE product(
    id_product INT,
    product_name VARCHAR(50),
    price NUMERIC(9,2)
) PARTITION BY RANGE (price);


/*Creamos las tablas secundarias de client*/
CREATE TABLE client_partiton_1 PARTITION OF client FOR VALUES IN ('Male', 'MALE');
CREATE TABLE client_partiton_2 PARTITION OF client FOR VALUES IN ('Female', 'FEMALE');

/*Creamos las tablas secundarias de product*/
CREATE TABLE product_partition_1 PARTITION OF product FOR VALUES FROM (1.00) TO (3000.99);
CREATE TABLE product_partition_2 PARTITION OF product FOR VALUES FROM (3001.00) TO (6000.99);
CREATE TABLE product_partition_3 PARTITION OF product FOR VALUES FROM (6001.00) TO (10000.00);

/*Creamos las restricciones de client*/
ALTER TABLE client_partiton_1 ADD CONSTRAINT client_partition_1_check CHECK (gender = 'Male' OR gender = 'MALE');
ALTER TABLE client_partiton_2 ADD CONSTRAINT client_partition_2_check CHECK (gender = 'Female' OR gender = 'FEMALE');

/*Creamos las restricciones de product*/
ALTER TABLE product_partition_1 ADD CONSTRAINT product_partition_1_check CHECK (price >= 1.00 AND price <= 3000.99);
ALTER TABLE product_partition_2 ADD CONSTRAINT product_partition_2_check CHECK (price >= 3001.00 AND price <= 6000.99);
ALTER TABLE product_partition_3 ADD CONSTRAINT product_partition_3_check CHECK (price >= 6001.00 AND price <= 10000.00);