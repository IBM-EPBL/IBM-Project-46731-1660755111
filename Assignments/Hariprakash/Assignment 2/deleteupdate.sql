create database user_details
use user_details 
create table team
(
userID int primary key,
username varchar(50),
password varchar(50),
email varchar(50),
rollno int
)
insert into team values (1,'bala vignesh','vignesh20','vignesh@gmail.com',713319CS020);
insert into team values (2,'Harish','harish40','harish@gmail.com',713319CS040);
insert into team values (3,'Hariprakash','hari39','hari@gmail.com',713319CS039);
insert into team values (4,'Gokul nathan','gokul30','gokul@gmail.com',713319CS030);
select*from team
delete from team where userID=4
update team set username='Saran' where userID=4