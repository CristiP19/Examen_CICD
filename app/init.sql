CREATE DATABASE IF NOT EXISTS myapp_base;
USE myapp_base;

CREATE TABLE IF NOT EXISTS shoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    image VARCHAR(100) NOT NULL
);

INSERT INTO shoes (name, description, price, image) VALUES
('Nike Air Max', 'Pantofi sport de calitate superioară', 599.99, 'nike_air_max.jpg'),
('Adidas Superstar', 'Clasici Adidas cu vârf shell toe', 449.99, 'adidas_superstar.jpg'),
('Timberland', 'Ghete rezistente la apă', 799.99, 'timberland.jpg');