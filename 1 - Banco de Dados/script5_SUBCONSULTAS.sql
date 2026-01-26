INSERT INTO destinos(nome, descricao) VALUES ("Destino sem reserva", "Descricao");
##Trazer destinos que não tem reservas, destinos menos populares - Sub Consultas
SELECT * FROM destinos
WHERE id NOT IN(SELECT id_destino FROM reservas);

#Sub Consulta
SELECT nome, (SELECT COUNT(*) FROM reservas WHERE id_usuario = usuarios.id) AS total_reservas
FROM usuarios;