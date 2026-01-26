select * from usuarios;

##Adicionando as colunas referentes as informações do endereço. No 'ADD' não precisa especificar que é uma coluna, palavra 'COLUMN'
ALTER TABLE usuarios
ADD rua VARCHAR(100), 
ADD numero VARCHAR(10),
ADD cidade VARCHAR(50),
ADD estado VARCHAR(20);
##Padronizando o endereço na forma como foi colocado na aula 
UPDATE usuarios SET endereco = 'Street, 5468, São Paulo, São Paulo' WHERE id=2;

##Script para inserção de valores nas colunas novas utilizando o SUBSTRING, lembrando que nesse caso da certo, pois as informações foram adicionadas mantendo um padrão: rua, numero, cidade e estado
UPDATE usuarios
SET rua = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 1), ',', -1),
	numero = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 2), ',', -1),
    cidade = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 3), ',', -1),
    estado = SUBSTRING_INDEX(endereco, ',', -1);
    
##Continuando a normalização: exclusão da coluna inicial 'endereco'
ALTER TABLE usuarios
DROP COLUMN endereco;

