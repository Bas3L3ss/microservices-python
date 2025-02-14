create user 'sa'@'localhost' identified by 'sa123';

create database auth;

grant all PRIVILEGES on auth.* to 'sa'@'localhost';

use auth;

create table user(
    id INT not null auto_increment primary key,
    email varchar(255) not null,
    password varchar(255) not null,
);

INSERT INTO user (email, password) VALUES ('sa', 'sa123');