SELECT * FROM card_holder;
SELECT * FROM credit_card;
SELECT * FROM merchant;
SELECT * FROM merchant_category;
SELECT * FROM transaction;

SELECT date_trunc('day',date), card_holder_id, COUNT(*) FROM transaction t
INNER JOIN credit_card cc ON cc.credit_card_number = t.credit_card_number
WHERE card_holder_id = 2 OR card_holder_id = 18
GROUP BY date_trunc('day',date),card_holder_id
ORDER BY date_trunc('day',date);

SELECT date, SUM(amount) FROM transaction t
INNER JOIN credit_card cc ON cc.credit_card_number = t.credit_card_number
WHERE card_holder_id = 25 AND date between '2018-01-01' AND '2018-07-01'
GROUP BY date;