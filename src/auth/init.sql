CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'Aauth123';

CREATE DATABASE auth;

GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';

USE auth;

CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

INSERT INTO user (email, password) VALUES ('keerthana@email.com', 'Admin123');
/*
mysql -uroot
    show databases;
    exit
mysql -uroot < init.sql
*queries if needed:
    mysql -uroot -e "DROP DATABASE auth" 
    mysql -uroot -e "DROP USER auth_user@localhost"

mysql -uroot
    show databases;
    use auth;
    show tables;
    describe user;
    select * from user;
    exit


*/

