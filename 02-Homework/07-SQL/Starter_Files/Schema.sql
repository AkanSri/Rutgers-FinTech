-- This script was generated by a beta version of the ERD tool in pgAdmin 4.
-- Please log an issue at https://redmine.postgresql.org/projects/pgadmin4/issues/new if you find any bugs, including reproduction steps.
BEGIN;
DROP TABLE IF EXISTS public.card_holder CASCADE;
DROP TABLE IF EXISTS public.credit_card CASCADE;
DROP TABLE IF EXISTS public.merchant CASCADE;
DROP TABLE IF EXISTS public.merchant_category CASCADE;
DROP TABLE IF EXISTS public.transaction CASCADE;

CREATE TABLE IF NOT EXISTS public.card_holder
(
    card_holder_id integer,
    card_holder_name character varying(50) NOT NULL,
    PRIMARY KEY (card_holder_id)
);

CREATE TABLE IF NOT EXISTS public.credit_card
(
    credit_card_number character varying(30),
    card_holder_id integer NOT NULL,
    PRIMARY KEY (credit_card_number)
);

CREATE TABLE IF NOT EXISTS public.merchant
(
    merchant_id integer,
    merchant_name character varying(50) NOT NULL,
    merchant_category_id integer NOT NULL,
    PRIMARY KEY (merchant_id)
);

CREATE TABLE IF NOT EXISTS public.merchant_category
(
    merchant_category_id integer,
    merchant_category_name character varying(30) NOT NULL,
    PRIMARY KEY (merchant_category_id)
);

CREATE TABLE IF NOT EXISTS public.transaction
(
    transaction_id integer,
    date timestamp without time zone NOT NULL,
    amount numeric(15, 2) NOT NULL,
    credit_card_number character varying(30) NOT NULL,
    merchant_id integer NOT NULL,
    PRIMARY KEY (transaction_id)
);

ALTER TABLE IF EXISTS public.credit_card
    ADD CONSTRAINT card_holder_id FOREIGN KEY (card_holder_id)
    REFERENCES public.card_holder (card_holder_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.merchant
    ADD CONSTRAINT fk_category_id FOREIGN KEY (merchant_category_id)
    REFERENCES public.merchant_category (merchant_category_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.transaction
    ADD CONSTRAINT fk_credit_card_number FOREIGN KEY (credit_card_number)
    REFERENCES public.credit_card (credit_card_number) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.transaction
    ADD CONSTRAINT fk_merchant_id FOREIGN KEY (merchant_id)
    REFERENCES public.merchant (merchant_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;