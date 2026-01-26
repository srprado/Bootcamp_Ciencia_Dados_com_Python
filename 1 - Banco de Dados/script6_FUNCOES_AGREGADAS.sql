USE viagens;

SELECT * FROM usuarios;
SELECT * FROM reservas;
SELECT * FROM destinos;

SELECT COUNT(*) as total_usuarios FROM usuarios us
INNER JOIN reservas rs ON us.id = rs.id_usuario;

INSERT INTO usuarios(nome, email, dataNascimento, rua, numero, cidade, estado) VALUES ("Maria Antônia", "mariantonia@email.com", "2000-11-02", "Rua 100", "568", "Jundiai", "SP");
INSERT INTO usuarios(nome, email, dataNascimento, rua, numero, cidade, estado) VALUES ("Carlos Augusto", "carlosaugusto@email.com", "1987-05-08", "Oliveira", "264", "Araraquara", "SP");
SELECT MAX(TIMESTAMPDIFF(YEAR, dataNascimento, CURRENT_DATE())) AS maior_idade FROM usuarios;

#confirmada, pendente, cancelada
INSERT INTO reservas(id_usuario, id_destino, dataReserva, status) VALUES(2, 1, "2026-12-08", "pendente");
INSERT INTO reservas(id_usuario, id_destino, dataReserva, status) VALUES(3, 2, "2027-02-15", "confirmada");
INSERT INTO reservas(id_usuario, id_destino, dataReserva, status) VALUES(4, 1, "2026-06-01", "cancelada");
INSERT INTO reservas(id_usuario, id_destino, dataReserva, status) VALUES(4, 1, "2026-08-01", "pendente");
SELECT COUNT(*), id_destino FROM reservas
GROUP BY id_destino;

SELECT id_destino, COUNT(*) AS qtd_reservas FROM reservas
GROUP BY id_destino
ORDER BY qtd_reservas ASC;
SELECT id_destino, COUNT(*) AS qtd_reservas FROM reservas
GROUP BY id_destino
ORDER BY qtd_reservas DESC;

