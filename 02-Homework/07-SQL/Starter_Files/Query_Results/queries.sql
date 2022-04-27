SELECT * FROM card_holder;
SELECT * FROM credit_card;
SELECT * FROM merchant;
SELECT * FROM merchant_category;
SELECT * FROM transaction;

--How can you isolate (or group) the transactions of each cardholder?
DROP VIEW IF EXISTS trans_each_holder;
CREATE VIEW trans_each_holder AS
SELECT card_holder_name, COUNT(transaction_id) as number_of_trans_per_holder FROM transaction t
INNER JOIN credit_card cc ON t.credit_card_number = cc.credit_card_number
INNER JOIN card_holder c ON cc.card_holder_id = c.card_holder_id
GROUP BY card_holder_name
ORDER BY number_of_trans_per_holder DESC;
SELECT * FROM trans_each_holder;

--Count the transactions that are less than $2.00 per cardholder.
DROP VIEW IF EXISTS trans_each_holder_less_2;
CREATE VIEW trans_each_holder_less_2 AS
SELECT card_holder_name, COUNT(t.transaction_id) as trans_count FROM transaction t
INNER JOIN credit_card cc ON t.credit_card_number = cc.credit_card_number
INNER JOIN card_holder c ON cc.card_holder_id = c.card_holder_id
WHERE amount <= 2.00
GROUP BY card_holder_name
ORDER BY trans_count DESC;
SELECT * FROM trans_each_holder_less_2;

--Top 100 highest transactions made between 7:00 am and 9:00 am
DROP VIEW IF EXISTS trans_bw_7_9;
CREATE VIEW trans_bw_7_9 AS
SELECT transaction_id, amount FROM transaction
WHERE date_part('hour',date) BETWEEN 7 AND 9
ORDER BY amount DESC
limit 100;
SELECT * FROM trans_bw_7_9;

--Number of fraudulent transactions made during between 7:00 am and 9:00 am 
--versus the rest of the day
DROP VIEW IF EXISTS trans_bw_7_9_others;
CREATE VIEW trans_bw_7_9_others AS
(SELECT COUNT(transaction_id), SUM(amount) FROM transaction
WHERE date_part('hour',date) BETWEEN 7 AND 9)
UNION ALL
(SELECT COUNT(transaction_id), SUM (amount) FROM transaction
WHERE date_part('hour',date) NOT BETWEEN 7 AND 9);
SELECT * FROM trans_bw_7_9_others;

--top 5 merchants prone to being hacked using small transactions 
DROP VIEW IF EXISTS top_5_merchants;
CREATE VIEW top_5_merchants AS
SELECT merchant_name, COUNT(t.transaction_id) as trans_count FROM transaction t
INNER JOIN merchant m ON t.merchant_id = m.merchant_id
WHERE amount <= 2.00
GROUP BY merchant_name
ORDER BY trans_count DESC
LIMIT 5;
SELECT * FROM top_5_merchants;
