
create database Employee

CREATE TABLE Employee (
  id INT Identity(1,1) PRIMARY KEY,
  firstname varchar (100),
  lastname varchar (100) ,
  salary INT 
);
 insert  into Employee(firstname , lastname ,salary )
 VALUES ( 'Ali' , 'Ahmed' , 5001 ),
		( 'Omer' , 'Ahmed' , 10000 ),
		( 'Ali' , 'Ahmed' , 1000 );

SELECT firstname,lastname,salary
from Employee 
WHERE salary > 5000;