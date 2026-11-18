-- Datos de ejemplo para academia_python
USE claseSimulacro;

-- Cursos
INSERT INTO curso (curso_id, nombre, duracion_horas, precio) VALUES
(1, 'Python y Bases de Datos', 90, 450.00),
(2, 'Java y Spring Boot', 120, 600.00),
(3, 'Desarrollo Web', 80, 400.00),
(4, 'Acceso a Datos', 100, 500.00);

-- Alumnos
INSERT INTO alumno (nia, nombre, apellidos, email, fecha_nacimiento) VALUES
(1001, 'Lucia', 'Garcia Lopez', 'lucia.garcia@example.com', '2004-03-14'),
(1002, 'Marcos', 'Perez Ruiz', 'marcos.perez@example.com', '2003-11-22'),
(1003, 'Sara', 'Martinez Gil', 'sara.martinez@example.com', '2004-07-09'),
(1004, 'Daniel', 'Sanchez Torres', 'daniel.sanchez@example.com', '2003-01-30'),
(1005, 'Nerea', 'Romero Diaz', 'nerea.romero@example.com', '2004-12-05');

-- Profesores
INSERT INTO profesor (profesor_id, nombre, apellidos, especialidad) VALUES
(1, 'Ana', 'Lopez Martin', 'Python'),
(2, 'Carlos', 'Navarro Perez', 'Java'),
(3, 'Elena', 'Ruiz Sanchez', 'Bases de Datos');

-- Matrículas: al final porque dependen de alumnos y cursos
INSERT INTO matricula (matricula_id, nia, curso_id, fecha_matricula, nota) VALUES
(1, 1001, 1, '2026-09-10', 8.50),
(2, 1002, 2, '2026-09-11', 7.25),
(3, 1003, 1, '2026-09-12', 9.10),
(4, 1004, 3, '2026-09-13', 6.75),
(5, 1005, 4, '2026-09-14', 8.00),
(6, 1001, 2, '2026-09-15', 7.80),
(7, 1003, 3, '2026-09-16', 9.40);
