
/*  source C:\Users\baris\Desktop\deneme2\Database\code.sql   */

/* 1-Creating database called hotel */
drop database if exists hotel;
create database hotel;
/* Using this command to make operations on hotel database */
use hotel;

/*CREATING TABLES*/
create table room(
    room_ID int not null,
    room_price int,
    room_info varchar(10),
    available_date date,
    primary key (room_ID)
);

/*FILLING TABLE WITH DATA*/
insert into room values (1,2,"Single","2020-06-15");
insert into room values (2,4,"Double","2020-01-17");
insert into room values (3,6,"Deluxe","2020-09-05");
insert into room values (4,8,"KingSuit","2020-12-31");
insert into room values (5,10,"PASHA","2021-06-18");


