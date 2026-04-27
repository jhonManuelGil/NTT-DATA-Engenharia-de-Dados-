-- Active: 1777250545185@@127.0.0.1@5432@postgres

CREATE TABLE productos (
    id INT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0
);

SELECT * FROM productos;

CREATE TABLE productos (
    id INT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0
);
