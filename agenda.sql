--
-- PostgreSQL database dump
--

-- Dumped from database version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)

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
-- Name: conference; Type: TABLE; Schema: public; Owner: michel
--

CREATE TABLE public.conference (
    conference_id integer NOT NULL,
    title character varying(250) NOT NULL,
    summary character varying(250) NOT NULL,
    date date NOT NULL,
    hour time without time zone NOT NULL,
    speaker_id integer,
    creation_date timestamp without time zone
);


ALTER TABLE public.conference OWNER TO michel;

--
-- Name: conference_conference_id_seq; Type: SEQUENCE; Schema: public; Owner: michel
--

CREATE SEQUENCE public.conference_conference_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.conference_conference_id_seq OWNER TO michel;

--
-- Name: conference_conference_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: michel
--

ALTER SEQUENCE public.conference_conference_id_seq OWNED BY public.conference.conference_id;


--
-- Name: events; Type: TABLE; Schema: public; Owner: michel
--


CREATE TABLE public.speaker (
    speaker_id integer NOT NULL,
    last_name character varying(50) NOT NULL,
    first_name character varying(50) NOT NULL,
    description character varying(50) NOT NULL,
    status boolean DEFAULT true,
    job character varying(50) NOT NULL
);


ALTER TABLE public.speaker OWNER TO michel;

--
-- Name: speaker_speaker_id_seq; Type: SEQUENCE; Schema: public; Owner: michel
--

CREATE SEQUENCE public.speaker_speaker_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.speaker_speaker_id_seq OWNER TO michel;

--
-- Name: speaker_speaker_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: michel
--

ALTER SEQUENCE public.speaker_speaker_id_seq OWNED BY public.speaker.speaker_id;


--
-- Name: conference conference_id; Type: DEFAULT; Schema: public; Owner: michel
--

ALTER TABLE ONLY public.conference ALTER COLUMN conference_id SET DEFAULT nextval('public.conference_conference_id_seq'::regclass);


--
-- Name: speaker speaker_id; Type: DEFAULT; Schema: public; Owner: michel
--

ALTER TABLE ONLY public.speaker ALTER COLUMN speaker_id SET DEFAULT nextval('public.speaker_speaker_id_seq'::regclass);


--
-- Data for Name: conference; Type: TABLE DATA; Schema: public; Owner: michel
--

COPY public.conference (conference_id, title, summary, date, hour, speaker_id, creation_date) FROM stdin;
\.


--
-- Data for Name: events; Type: TABLE DATA; Schema: public; Owner: michel
--



--
-- Data for Name: speaker; Type: TABLE DATA; Schema: public; Owner: michel
--

COPY public.speaker (speaker_id, last_name, first_name, description, status, job) FROM stdin;
\.


--
-- Name: conference_conference_id_seq; Type: SEQUENCE SET; Schema: public; Owner: michel
--

SELECT pg_catalog.setval('public.conference_conference_id_seq', 1, false);


--
-- Name: events_id_event_seq; Type: SEQUENCE SET; Schema: public; Owner: michel
--

SELECT pg_catalog.setval('public.events_id_event_seq', 9, true);


--
-- Name: speaker_speaker_id_seq; Type: SEQUENCE SET; Schema: public; Owner: michel
--

SELECT pg_catalog.setval('public.speaker_speaker_id_seq', 1, false);


--
-- Name: conference conference_pkey; Type: CONSTRAINT; Schema: public; Owner: michel
--

ALTER TABLE ONLY public.conference
    ADD CONSTRAINT conference_pkey PRIMARY KEY (conference_id);



--
-- Name: speaker speaker_pkey; Type: CONSTRAINT; Schema: public; Owner: michel
--

ALTER TABLE ONLY public.speaker
    ADD CONSTRAINT speaker_pkey PRIMARY KEY (speaker_id);


--
-- Name: conference conference_speaker_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: michel
--

ALTER TABLE ONLY public.conference
    ADD CONSTRAINT conference_speaker_id_fkey FOREIGN KEY (speaker_id) REFERENCES public.speaker(speaker_id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

