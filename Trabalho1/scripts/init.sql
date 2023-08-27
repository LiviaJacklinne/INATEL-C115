--  definição do esquema de criação da tabela
create database trabalho1;

-- estabelecendo a conexão com o banco
\c trabalho1;

-- Criando a tabela
create table perguntas(
    id serial not null,
    respostas VARCHAR(100) NOT NULL 
);