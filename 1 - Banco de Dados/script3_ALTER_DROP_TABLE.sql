create table usuarios_nova(
	id int,
    nome varchar(255) not null comment 'Nome do usuário',
    email varchar(100) not null unique comment 'E-mail do usuario',
    endereco varchar(100) not null comment 'Endereço do usuario',
    dataNascimento date not null comment 'Data de nascimento do usuario'
);
select * from usuarios_nova;

##Migrando os dados da tabela antiga para a tabela nova
INSERT INTO usuarios_nova(id, nome, email, endereco, dataNascimento) SELECT id, nome, email, endereco, dataNascimento FROM usuarios;

##Excluindo a tabela permanentemente
DROP TABLE usuarios;

##Alterando o nome da nova tabela
ALTER TABLE usuarios_nova RENAME usuarios;
ALTER TABLE usuarios MODIFY COLUMN endereco VARCHAR(150);
SELECT * FROM usuarios;

##Adicionando chave primária nas tabelas
ALTER TABLE usuarios MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY(id);

SELECT * FROM destinos;
ALTER TABLE destinos MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY(id);

SELECT * FROM reservas;
ALTER TABLE reservas MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY(id);

ALTER TABLE reservas 
ADD CONSTRAINT fk_reservas_usuarios
FOREIGN KEY(id_usuario) REFERENCES usuarios(id);

ALTER TABLE reservas 
ADD CONSTRAINT fk_reservas_destinos
FOREIGN KEY(id_destino) REFERENCES destinos(id);
#ao rodar destinos deu 'Error Code: 1452', isto é, quando você tentou criar a foreign key, o MySQL verificou os dados que já existem na tabela reservas e encontrou valores em reservas.id_destino que não existem em destinos.id, 
#ou seja, existem reservas apontando para destinos inexistentes, por isso irei adicionar registro na tabela de destinos. Não precisa mais adicionar id, pois nesse ponto ele já é auto_increment
INSERT INTO destinos(nome, descricao) VALUES ( "Praia das Rosas", "Praia");
#Depois da linha de cima, rodar novamente o alter table de 'reservas' para adicionar a FK de destinos
SELECT * FROM reservas;
SELECT * FROM destinos;
#Agora ao inserir um dado na tabela de reservas é necessário que o resgitro exista na tabela de 'usuarios' e na tabela de 'destinos'

##Alterando a tabela de reservas para que as informações sejam CASCADE, isto é, ao excluir o registro pai(id-primary key) os filhos serão excluidos também(id - foreign key)
ALTER TABLE reservas
ADD CONSTRAINT fk_usuarios
FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
ON DELETE CASCADE;
#deu erro em cima pois ficou 2 constraints para a msm alteração/inserção de FK, rodar o código abaixo
ALTER TABLE reservas DROP CONSTRAINT fk_reservas_usuarios;
#Agora sim rodar o código abaixo, recriando a constraint, porém agora com o delete cascade:
ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_usuarios
FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
ON DELETE CASCADE;

##Agora excluindo um resgitro pai
DELETE FROM usuarios WHERE id = 1;
##Agora o registro com o usuario de id=1 também foi deletado da tabela de 'reservas'
SELECT * FROM reservas;
##CUIDADO COM O USO DO CASCADE##































