/*CREATE SCHEMA viagens;*/

create table usuarios(
	id int,
    nome varchar(255) not null comment 'Nome do usuário',
    email varchar(100) not null unique comment 'E-mail do usuario',
    endereco varchar(50) not null comment 'Endereço do usuario',
    dataNascimento date not null comment 'Data de nascimento do usuario'
);

create table destinos(
	id int,
    nome varchar(255) not null unique,
    descricao varchar(255) not null
);

create table reservas(
	id int,
    id_usuario int,
    id_destino int,
    dataReserva DATE,
    status varchar(255) default 'pendente' comment 'Status da reserva (confirmada, pendente, cancelada etc.)'
);