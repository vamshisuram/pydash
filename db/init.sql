CREATE DATABASE IF NOT EXISTS employee;
USE employee;

CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(50) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Salary INT NOT NULL
);

INSERT INTO Employees (FirstName, LastName, Email, Phone, Salary)
VALUES ('John', 'Doe', 'john.doe@email.com', '123-456-7890', 60000),
       ('Jane', 'Smith', 'jane.smith@email.com', '555-555-5555', 70000),
       ('Bob', 'Jones', 'bob.jones@email.com', '111-222-3333', 50000),
       ('Sarah', 'Lee', 'sarah.lee@email.com', '444-444-4444', 80000),
       ('Mike', 'Smith', 'mike.smith@email.com', '777-777-7777', 65000);

CREATE USER 'regular'@'localhost' IDENTIFIED BY 'pass';
GRANT ALL PRIVILEGES ON employee.* TO 'regular'@'localhost';