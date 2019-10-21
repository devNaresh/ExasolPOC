USE poc;
LOAD DATA INFILE '/Users/aravindraj/data_for_mysql/instacart/aisles.csv' INTO TABLE aisles FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
LOAD DATA INFILE '/Users/aravindraj/data_for_mysql/instacart/departments.csv' INTO TABLE departments FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
LOAD DATA INFILE '/Users/aravindraj/data_for_mysql/instacart/orders.csv' INTO TABLE orders FIELDS TERMINATED BY ',' ENCLOSED BY '\'' LINES TERMINATED BY '\n' IGNORE 1 ROWS (order_id,user_id,eval_set,order_number,order_dow,order_hour_of_day,@days_since_prior_order) SET days_since_prior_order = nullif(@days_since_prior_order,'');
LOAD DATA INFILE '/Users/aravindraj/data_for_mysql/instacart/products.csv' INTO TABLE products FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS; 
LOAD DATA INFILE '/Users/aravindraj/data_for_mysql/instacart/order_products__prior.csv' INTO TABLE order_products FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
LOAD DATA INFILE '/Users/aravindraj/data_for_mysql/instacart/order_products__train.csv' INTO TABLE order_products FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
ALTER TABLE orders ADD order_date DATETIME;
UPDATE
  `orders`
SET
  order_date = FROM_UNIXTIME(
    UNIX_TIMESTAMP('2017-10-15 14:53:27') + FLOOR(0 + (RAND() * 63072000)));
ALTER TABLE orders DROP eval_set;
