#CREATE
INSERT INTO usuarios(id, nome, email, endereco, dataNascimento) VALUES (1,"Sabrina Prado", "sabrinaprado@email.com", "Rua das Rosas, 100", "1999-10-26");
INSERT INTO usuarios(id, nome, email, endereco, dataNascimento) VALUES (2,"José Júnior", "josejunior@email.com", "Street, 5468", "1985-01-25");
/*testes para comando unique, not null e default*/
INSERT INTO destinos(id, nome, descricao) VALUES (1, "Praia das Rosas", "Praia");

INSERT INTO reservas(id, id_usuario, id_destino, dataReserva, status) VALUES (1, 1, 1, "2026-10-01", "pendente");

#READ
SELECT * FROM usuarios;
SELECT * FROM usuarios WHERE id=1 AND nome LIKE "%Sab%";
SELECT * FROM destinos;
SELECT * FROM reservas;
/*usar o WHERE para filtrar registros*/

#UPDATE
UPDATE usuarios SET nome = "Maria" WHERE id=1;
UPDATE usuarios SET email = "maria@email.com" WHERE id=1;
SELECT * FROM usuarios;

#DELETE
DELETE FROM destinos WHERE nome = "Praia das Rosas";
SELECT * FROM destinos;