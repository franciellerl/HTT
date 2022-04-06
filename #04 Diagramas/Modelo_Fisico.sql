--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2
-- Dumped by pg_dump version 14.2

-- Started on 2022-04-05 23:14:28

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

CREATE DATABASE "Modelo_Fisico" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Portuguese_Brazil.1252';
\connect "Modelo_Fisico"

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';
SET default_table_access_method = heap;

CREATE TABLE public."Aluguel" (
    "ID_Imovel" integer,
    "ID_Aluguel" integer NOT NULL,
    "ID_Inquilino" integer
);
ALTER TABLE public."Aluguel" OWNER TO postgres;

CREATE TABLE public."Contrato" (
    "ID_Contrato" integer NOT NULL,
    "ID_Aluguel" integer,
    "Valor" integer
);
ALTER TABLE public."Contrato" OWNER TO postgres;

CREATE TABLE public."Corretor" (
    "ID_Corretor" integer NOT NULL
);
ALTER TABLE public."Corretor" OWNER TO postgres;

CREATE TABLE public."Imovel" (
    "ID_Imovel" integer NOT NULL,
    "Logradouro" "char",
    "CEP" integer,
    "Bairro" "char",
    "Cidade" "char"
);
ALTER TABLE public."Imovel" OWNER TO postgres;

CREATE TABLE public."Inquilino" (
    "ID_Inquilino" integer NOT NULL,
    "Nome" "char",
    "DataNascimento" "char"
);
ALTER TABLE public."Inquilino" OWNER TO postgres;


CREATE TABLE public."Proprietario" (
    "ID_Proprietario" integer NOT NULL,
    "Nome" "char",
    "DataNascimento" "char"
);
ALTER TABLE public."Proprietario" OWNER TO postgres;


ALTER TABLE ONLY public."Aluguel"
    ADD CONSTRAINT "Aluguel_pkey" PRIMARY KEY ("ID_Aluguel");

ALTER TABLE ONLY public."Contrato"
    ADD CONSTRAINT "Contrato_pkey" PRIMARY KEY ("ID_Contrato");

ALTER TABLE ONLY public."Corretor"
    ADD CONSTRAINT "Corretor_pkey" PRIMARY KEY ("ID_Corretor");

ALTER TABLE ONLY public."Imovel"
    ADD CONSTRAINT "Imovel_pkey" PRIMARY KEY ("ID_Imovel");

ALTER TABLE ONLY public."Inquilino"
    ADD CONSTRAINT "Inquilino_pkey" PRIMARY KEY ("ID_Inquilino");

ALTER TABLE ONLY public."Proprietario"
    ADD CONSTRAINT "Proprietario_pkey" PRIMARY KEY ("ID_Proprietario");
    
ALTER TABLE ONLY public."Aluguel"
    ADD CONSTRAINT "ID_Aluguel" FOREIGN KEY ("ID_Imovel") REFERENCES public."Imovel"("ID_Imovel");

ALTER TABLE ONLY public."Contrato"
    ADD CONSTRAINT "ID_Aluguel" FOREIGN KEY ("ID_Aluguel") REFERENCES public."Aluguel"("ID_Aluguel");

ALTER TABLE ONLY public."Aluguel"
    ADD CONSTRAINT "ID_Inquilino" FOREIGN KEY ("ID_Inquilino") REFERENCES public."Inquilino"("ID_Inquilino");

GRANT ALL ON TABLE public."Aluguel" TO PUBLIC;
GRANT ALL ON TABLE public."Contrato" TO PUBLIC;
GRANT ALL ON TABLE public."Corretor" TO PUBLIC;
GRANT ALL ON TABLE public."Imovel" TO PUBLIC;
GRANT ALL ON TABLE public."Inquilino" TO PUBLIC;
GRANT ALL ON TABLE public."Proprietario" TO PUBLIC;

-- Completed on 2022-04-05 23:14:29

--
-- PostgreSQL database dump complete
--
