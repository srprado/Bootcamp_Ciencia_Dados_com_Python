create table usuarios_nova(
	id int,
    nome varchar(255) not null comment 'Nome do usuário',
    email varchar(100) not null unique comment 'E-mail do usuario',
    endereco varchar(100) not null comment 'Endereço do usuario',
    dataNascimento date not null comment 'Data de nascimento do usuario'
);
select * from usuarios_nova;

#Migrando os dados da tabela antiga para a tabela nova
INSERT INTO usuarios_nova(id, nome, email, endereco, dataNascimento) SELECT id, nome, email, endereco, dataNascimento FROM usuarios;

#Excluindo a tabela permanentemente
DROP TABLE usuarios;

#Alterando o nome da nova tabela
ALTER TABLE usuarios_nova RENAME usuarios;
ALTER TABLE usuarios MODIFY COLUMN endereco VARCHAR(150);

