CREATE DATABASE IF NOT EXISTS sales_db;

USE sales_db;

CREATE TABLE IF NOT EXISTS sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product VARCHAR(50),
    quantity INT,
    price DECIMAL(10,2)
);

INSERT INTO sales (product, quantity, price) VALUES 
('Apple', 10, 0.5),
('Banana', 20, 0.3),
('Apple', 15, 0.5),
('Orange', 25, 0.4),
('Banana', 30, 0.3),
('Orange', 10, 0.4);
