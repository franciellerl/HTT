--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2
-- Dumped by pg_dump version 14.2

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

--
-- Name: crud_htt; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE crud_htt WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Portuguese_Brazil.1252';
\connect crud_htt

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

CREATE TABLE public.aluguel (
    id integer NOT NULL,
    "idImovel" integer,
    "idProp" integer,
    num_contrato integer
);
ALTER TABLE public.aluguel OWNER TO postgres;

CREATE TABLE public.imovel (
    id integer NOT NULL,
    lougradouro character varying,
    cep character varying,
    bairro character varying,
    cidade character varying
);
ALTER TABLE public.imovel OWNER TO postgres;

CREATE TABLE public.inquilino (
    id integer NOT NULL,
    nome character varying,
    data_nascimento character varying
);
ALTER TABLE public.inquilino OWNER TO postgres;


CREATE TABLE public.proprietario (
    id integer NOT NULL,
    nome character varying,
    data_nascimento character varying
);
ALTER TABLE public.proprietario OWNER TO postgres;

ALTER TABLE ONLY public.aluguel ALTER COLUMN id SET DEFAULT nextval('public.aluguel_id_seq'::regclass);

ALTER TABLE ONLY public.imovel ALTER COLUMN id SET DEFAULT nextval('public.imovel_id_seq'::regclass);

ALTER TABLE ONLY public.inquilino ALTER COLUMN id SET DEFAULT nextval('public.inquilino_id_seq'::regclass);

ALTER TABLE ONLY public.proprietario ALTER COLUMN id SET DEFAULT nextval('public.proprietario_id_seq'::regclass);


COPY public.aluguel (id, "idImovel", "idProp", num_contrato) FROM stdin;
10	\N	\N	12345
\.

COPY public.imovel (id, lougradouro, cep, bairro, cidade) FROM stdin;
2	slz	slz	slz	slz
1	nyc	nyc	nyc	nyc
\.

COPY public.inquilino (id, nome, data_nascimento) FROM stdin;
1	oi	oi
13	eu	eu
9	olarb	olarb
\.

COPY public.proprietario (id, nome, data_nascimento) FROM stdin;
5	ssssss	dd
7	mart	reffe
8	ola	ola
\.

SELECT pg_catalog.setval('public.aluguel_id_seq', 10, true);

SELECT pg_catalog.setval('public.imovel_id_seq', 2, true);

SELECT pg_catalog.setval('public.inquilino_id_seq', 13, true);

SELECT pg_catalog.setval('public.proprietario_id_seq', 8, true);

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);

ALTER TABLE ONLY public.aluguel
    ADD CONSTRAINT aluguel_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.imovel
    ADD CONSTRAINT imovel_pkey PRIMARY KEY (id);
    
ALTER TABLE ONLY public.inquilino
    ADD CONSTRAINT inquilino_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.proprietario
    ADD CONSTRAINT proprietario_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.aluguel
    ADD CONSTRAINT "aluguel_idImovel_fkey" FOREIGN KEY ("idImovel") REFERENCES public.imovel(id);

ALTER TABLE ONLY public.aluguel
    ADD CONSTRAINT "aluguel_idProp_fkey" FOREIGN KEY ("idProp") REFERENCES public.proprietario(id);


--
-- PostgreSQL database dump complete
--

