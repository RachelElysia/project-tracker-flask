--
-- PostgreSQL database dump
--

-- Dumped from database version 10.15 (Ubuntu 10.15-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.15 (Ubuntu 10.15-0ubuntu0.18.04.1)

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
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: grades; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.grades (
    id integer NOT NULL,
    student_github character varying(30),
    project_title character varying(30),
    grade integer
);


ALTER TABLE public.grades OWNER TO vagrant;

--
-- Name: grades_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.grades_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.grades_id_seq OWNER TO vagrant;

--
-- Name: grades_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.grades_id_seq OWNED BY public.grades.id;


--
-- Name: projects; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.projects (
    id integer NOT NULL,
    title character varying(30),
    description text,
    max_grade integer
);


ALTER TABLE public.projects OWNER TO vagrant;

--
-- Name: projects_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.projects_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.projects_id_seq OWNER TO vagrant;

--
-- Name: projects_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.projects_id_seq OWNED BY public.projects.id;


--
-- Name: students; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.students (
    id integer NOT NULL,
    first_name character varying(30),
    last_name character varying(30),
    github character varying(30)
);


ALTER TABLE public.students OWNER TO vagrant;

--
-- Name: students_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.students_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.students_id_seq OWNER TO vagrant;

--
-- Name: students_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.students_id_seq OWNED BY public.students.id;


--
-- Name: grades id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.grades ALTER COLUMN id SET DEFAULT nextval('public.grades_id_seq'::regclass);


--
-- Name: projects id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.projects ALTER COLUMN id SET DEFAULT nextval('public.projects_id_seq'::regclass);


--
-- Name: students id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.students ALTER COLUMN id SET DEFAULT nextval('public.students_id_seq'::regclass);


--
-- Data for Name: grades; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.grades (id, student_github, project_title, grade) FROM stdin;
1	jhacks	Markov	10
2	jhacks	Blockly	2
3	sdevelops	Blockly	100
4	sdevelops	Markov	50
\.


--
-- Data for Name: projects; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.projects (id, title, description, max_grade) FROM stdin;
1	Markov	Tweets generated from Markov chains	50
2	Blockly	Programmatic Logic Puzzle Game	10
5	Wits and Wagers	Bidding Game	150
\.


--
-- Data for Name: students; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.students (id, first_name, last_name, github) FROM stdin;
1	Jane	Hacker	jhacks
2	Sarah	Developer	sdevelops
3	ilana	mercer	ilanam
4	rachel	perkins	rperkins
5	rachel	perkins	rperkins
6	yo	cat	yocat
\.


--
-- Name: grades_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.grades_id_seq', 4, true);


--
-- Name: projects_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.projects_id_seq', 5, true);


--
-- Name: students_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.students_id_seq', 6, true);


--
-- Name: grades grades_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.grades
    ADD CONSTRAINT grades_pkey PRIMARY KEY (id);


--
-- Name: projects projects_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_pkey PRIMARY KEY (id);


--
-- Name: students students_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

