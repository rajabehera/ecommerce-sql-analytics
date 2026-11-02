CREATE TABLE customers (
  customer_id INT PRIMARY KEY, name TEXT, email TEXT,
  city TEXT, signup_date DATE
);
CREATE TABLE orders (
  order_id INT, customer_id INT, order_date DATE,
  amount NUMERIC(10,2), status TEXT
);