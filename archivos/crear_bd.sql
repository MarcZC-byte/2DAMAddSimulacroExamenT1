-- Crear base de datos para el simulacro ADD
DROP DATABASE IF EXISTS claseSimulacro;
CREATE DATABASE claseSimulacro;
USE claseSimulacro;

CREATE TABLE curso (
    curso_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    duracion_horas INT NOT NULL,
    precio DECIMAL(8,2) NOT NULL
);

CREATE TABLE alumno (
    nia INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE,
    fecha_nacimiento DATE
);

CREATE TABLE profesor (
    profesor_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(150) NOT NULL,
    especialidad VARCHAR(100)
);

CREATE TABLE matricula (
    matricula_id INT AUTO_INCREMENT PRIMARY KEY,
    nia INT NOT NULL,
    curso_id INT NOT NULL,
    fecha_matricula DATE NOT NULL,
    nota DECIMAL(4,2),
    CONSTRAINT fk_matricula_alumno FOREIGN KEY (nia) REFERENCES alumno(nia),
    CONSTRAINT fk_matricula_curso FOREIGN KEY (curso_id) REFERENCES curso(curso_id)
);
