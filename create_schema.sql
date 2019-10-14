CREATE DATABASE poc;
USE poc;
CREATE TABLE aisles (
  aisle_id INT NOT NULL AUTO_INCREMENT,
  aisle VARCHAR(200) NOT NULL,
  PRIMARY KEY(aisle_id)
);
CREATE TABLE departments (
  department_id INT NOT NULL AUTO_INCREMENT,
  department VARCHAR(200) NOT NULL,
  PRIMARY KEY(department_id)
);
CREATE TABLE orders (
  order_id INT NOT NULL AUTO_INCREMENT,
  user_id INT NOT NULL,
  eval_set VARCHAR(10),
  order_number INT,
  order_dow INT,
  order_hour_of_day INT,
  days_since_prior_order INT,
  PRIMARY KEY(order_id)
);
CREATE TABLE products (
  product_id INT NOT NULL AUTO_INCREMENT,
  product_name TEXT,
  aisle_id INT,
  department_id INT,
  PRIMARY KEY(product_id),
  FOREIGN KEY(aisle_id) REFERENCES aisles(aisle_id),
  FOREIGN KEY(department_id) REFERENCES departments(department_id)
);
CREATE TABLE order_products (
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  add_to_cart_order INT,
  reordered INT
);
