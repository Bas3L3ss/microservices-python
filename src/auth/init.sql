create user 'auth_user'@'localhost' identified by 'sa123';

create database auth;

grant all PRIVILEGES on auth.* to 'auth_user'@'localhost';

use auth;

create table user(
    id INT not null auto_increment primary key,
    email varchar(255) not null unique,
    password varchar(255) not null
);

INSERT INTO user (email, password) VALUES ('sa', 'sa123');