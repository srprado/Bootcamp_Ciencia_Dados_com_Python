INSERT INTO usuarios (nome, email, dataNascimento, rua, numero, cidade, estado) VALUES
('Ana Souza', 'ana.souza@email.com', '1990-03-15', 'Rua das Flores', '120', 'São Paulo', 'SP'),
('Bruno Lima', 'bruno.lima@email.com', '1985-07-22', 'Av. Paulista', '850', 'São Paulo', 'SP'),
('Carla Mendes', 'carla.mendes@email.com', '1998-11-02', 'Rua Central', '45', 'Campinas', 'SP'),
('Daniel Rocha', 'daniel.rocha@email.com', '1979-01-10', 'Rua do Comércio', '300', 'Santos', 'SP'),
('Eduarda Pires', 'eduarda.pires@email.com', '2001-05-18', 'Rua Bela Vista', '77', 'Sorocaba', 'SP'),
('Felipe Araujo', 'felipe.araujo@email.com', '1993-09-09', 'Rua das Palmeiras', '560', 'Ribeirão Preto', 'SP'),
('Gabriela Nunes', 'gabriela.nunes@email.com', '1988-12-25', 'Av. Brasil', '1020', 'Rio de Janeiro', 'RJ'),
('Henrique Costa', 'henrique.costa@email.com', '1995-04-03', 'Rua das Acácias', '90', 'Niterói', 'RJ'),
('Isabela Freitas', 'isabela.freitas@email.com', '2000-06-30', 'Rua Nova', '15', 'Petrópolis', 'RJ'),
('João Martins', 'joao.martins@email.com', '1982-08-14', 'Rua Antiga', '430', 'Campos', 'RJ'),
('Karen Lopes', 'karen.lopes@email.com', '1997-02-21', 'Rua do Sol', '210', 'Belo Horizonte', 'MG'),
('Lucas Ribeiro', 'lucas.ribeiro@email.com', '1991-10-05', 'Av. Afonso Pena', '980', 'Belo Horizonte', 'MG'),
('Mariana Teixeira', 'mariana.teixeira@email.com', '1986-07-19', 'Rua Minas', '66', 'Contagem', 'MG'),
('Nathan Alves', 'nathan.alves@email.com', '2002-12-01', 'Rua Horizonte', '12', 'Betim', 'MG'),
('Olivia Barros', 'olivia.barros@email.com', '1994-03-27', 'Rua do Lago', '340', 'Uberlândia', 'MG'),
('Paulo Henrique', 'paulo.henrique@email.com', '1980-11-11', 'Rua das Pedras', '500', 'Curitiba', 'PR'),
('Quezia Moraes', 'quezia.moraes@email.com', '1999-01-08', 'Rua Paraná', '88', 'Londrina', 'PR'),
('Rafael Torres', 'rafael.torres@email.com', '1987-06-16', 'Av. Central', '760', 'Maringá', 'PR'),
('Sofia Guedes', 'sofia.guedes@email.com', '2003-04-24', 'Rua Jovem', '9', 'Ponta Grossa', 'PR'),
('Tiago Farias', 'tiago.farias@email.com', '1992-09-13', 'Rua Azul', '150', 'Porto Alegre', 'RS'),
('Ursula Klein', 'ursula.klein@email.com', '1984-02-02', 'Rua Germânica', '410', 'Novo Hamburgo', 'RS'),
('Victor Peixoto', 'victor.peixoto@email.com', '1996-05-07', 'Rua das Gaivotas', '205', 'Pelotas', 'RS'),
('Wesley Batista', 'wesley.batista@email.com', '1989-08-29', 'Av. Sul', '1000', 'Caxias do Sul', 'RS'),
('Xavier Monteiro', 'xavier.monteiro@email.com', '1978-12-17', 'Rua Antares', '333', 'Salvador', 'BA'),
('Yasmin Oliveira', 'yasmin.oliveira@email.com', '2001-07-01', 'Rua do Mar', '25', 'Ilhéus', 'BA'),
('Zeca Santos', 'zeca.santos@email.com', '1983-10-20', 'Rua do Porto', '610', 'Itabuna', 'BA'),
('Amanda Reis', 'amanda.reis@email.com', '1995-01-26', 'Rua Primavera', '70', 'Fortaleza', 'CE'),
('Bernardo Macedo', 'bernardo.macedo@email.com', '1988-04-12', 'Av. Beira Mar', '900', 'Fortaleza', 'CE'),
('Camila Duarte', 'camila.duarte@email.com', '1999-09-03', 'Rua das Dunas', '55', 'Caucaia', 'CE');

SELECT * FROM usuarios;
SELECT * FROM reservas;
SELECT * FROM destinos;

EXPLAIN
	SELECT * FROM usuarios WHERE email = "camila.duarte@email.com";
    
EXPLAIN
	SELECT * FROM usuarios WHERE nome = "João";
