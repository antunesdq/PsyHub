--Criando o banco.
CREATE SCHEMA `psi`;

--Usando o banco.
use `psi`;

--Criando a tabela "psicologo".
create table `psicologo` (
    `psi_id` INT NOT NULL AUTO_INCREMENT,
    `psi_nome` VARCHAR(40) NOT NULL,
    `psi_email` VARCHAR(40) NOT NULL,
    `psi_celular` VARCHAR(13) NOT NULL,
    `psi_senha` VARCHAR(20) NOT NULL,
    `psi_CPF` VARCHAR(15) NOT NULL,
    `psi_CRP` VARCHAR(15) NOT NULL,
    `psi_nascimento` DATE NOT NULL,
    `psi_endereco` VARCHAR(50) NOT NULL,
    PRIMARY KEY (ID) );

--Criando a tabela "paciente".
create table `paciente`(
    `pac_id` INT NOT NULL AUTO_INCREMENT,
    `pac_nome` VARCHAR(40) NOT NULL,
    `pac_email` VARCHAR(40) NOT NULL,
    `pac_celular` VARCHAR(13) NOT NULL,
    `pac_senha` VARCHAR(20) NOT NULL,
    `pac_CPF` VARCHAR(15) NOT NULL,
    `pac_nascimento` DATE NOT NULL,
    `pac_endereco` VARCHAR(50) NOT NULL,
    `psi_id` INT,
    `P1` VARCHAR(2200),
    `P2` VARCHAR(2200),
    `P3` VARCHAR(2200),
    `P4` VARCHAR(2200),
    `P5` VARCHAR(2200),
    `P6` VARCHAR(2200),
    `P7` VARCHAR(2200),
    `P8` VARCHAR(2200),
    `P9` VARCHAR(2200),
    `P12` VARCHAR(2200),
    `P13` VARCHAR(2200),
    `P14` VARCHAR(2200),
    `P15` VARCHAR(2200),
    `P16` VARCHAR(2200),
    `P17` VARCHAR(2200),
    `P18` VARCHAR(2200),
    `P19` VARCHAR(2200),
    `P20` VARCHAR(2200),
    `P21` VARCHAR(2200),
    `P22` VARCHAR(2200),
    `P23` VARCHAR(2200),
    `P24` VARCHAR(2200),
    `P25` VARCHAR(2200),
    `P26` VARCHAR(2200),
    `P27` VARCHAR(2200),
    `P28` VARCHAR(2200),
    `P29` VARCHAR(2200),
    `P30` VARCHAR(2200),
    `P31` VARCHAR(2200),
    `P32` VARCHAR(2200),
    `P33` VARCHAR(2200),
    `P34` VARCHAR(2200),
    `P35` VARCHAR(2200),
    `P36` VARCHAR(2200),
    `P37` VARCHAR(2200),
    `P38` VARCHAR(2200),
    `P39` VARCHAR(2200),
    `P40` VARCHAR(2200),
    `P41` VARCHAR(2200),
    `P42`VARCHAR(2200)
);

--Criando a tabela "evolucao".
create table `evolucao`(
    `evo_id` INT NOT NULL AUTO_INCREMENT,
    `pac_id` INT NOT NULL,
    `numero_sessao` INT NOT NULL,
    `datetime_inicio` DATETIME NOT NULL,
    `datetime_termino` DATETIME NOT NULL,
    `prodecimentos` VARCHAR(2200),
    `sintese` VARCHAR(2200),
    `observacao` VARCHAR(5000),
    `plan_prox_sessao` VARCHAR(2200)
)

--Adicionando um psicólogo.
INSERT INTO `psicologo`(
    `psi_nome`,
    `psi_email`,
    `psi_celular`,
    `psi_senha`,
    `psi_CPF`,
    `psi_CRP`,
    `psi_nascimento`,
    `psi_endereco`) VALUES();

-- Adicionando um paciente.
INSERT INTO `paciente`(
    `pac_nome`,
    `pac_email`,
    `pac_celular`,
    `pac_senha`,
    `pac_CPF`,
    `pac_nascimento`,
    `pac_endereco`,
    `pac_psicologo_id`) VALUES();

-- Adicionando uma sessão.
INSERT INTO `evolucao`(
    `evo_id`,
    `pac_id`,
    `numero_sessao`,
    `datetime_inicio`,
    `datetime_termino`,
    `prodecimentos`,
    `sintese`,
    `observacao`,
    `plan_prox_sessao`) VALUES();