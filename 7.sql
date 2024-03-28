create database Human_friends;
create table cats (
	id int auto_increment primary key,
	name varchar(200),
    birth_date date Not null,
    comands varchar(200)
    );
    create table dogs (
	id int auto_increment primary key,
	name varchar(200),
    birth_date date Not null,
    comands varchar(200)
    );
    create table humsters (
	id int auto_increment primary key,
	name varchar(200),
    birth_date date Not null,
    comands varchar(200)
    );
    create table camels (
	id int auto_increment primary key,
	name varchar(200),
    birth_date date Not null,
    comands varchar(200)
    );
    create table horses (
	id int auto_increment primary key,
	name varchar(200),
    birth_date date Not null,
    comands varchar(200)
    );
    create table donkies (
	id int auto_increment primary key,
	name varchar(200),
    birth_date date Not null,
    comands varchar(200)
    );
    insert into cats (name,birth_date,comands)
    values
    ('wiskers','2019-05-15','Sit,Pounce'),
    ('Smudge','2020-02-20','Sit,Pounce,Scratch'),
    ( 'Oliver','2020-06-30','Meow,Scretch, jump')
    ;
    insert into dogs (name,birth_date,comands)
    values
    ('Buddy','2018-12-10','Meow,Scretch, jump'),
    ('Fido','2020-01-01','Sit,Stay,Fetch'),
    ('Bella','2019-11-11','Sit,Stray,Roll')
    ;
    insert into humsters (name,birth_date,comands)
    values
    ('Peanut','2021-08-01','Spin,Roll'),
    ('Hammy','2021-03-10', 'Roll,Hide')
    ;
     insert into horses (name,birth_date,comands)
    values
    ('Tunder','2015-07-21','Trot,Canter,Gallop'),
    ('Storm','2014-05-05','Trot,Canter'),
    ('Blaze','2016-02-09','Trot,Jump,Gallop')
    ;
    insert into camels (name,birth_date,comands)
    values
    ('Sandy','2016-11-03','Walk Carry load' ),
    ('Dune','2018-12-12', 'Walk, Sit'),
    ('Sahara','2015-08-14','Walk,Run')
    ;
    insert into donkies (name,birth_date,comands)
    values
    ('Burro','2019-01-23','Walk,Bray,Kick'),
    ('Eeyore','2017-09-18','Walk,Bray')
    ;
    alter table cats 
		add column type varchar(200) default 'cat';
	alter table dogs 
		add column type varchar(200) default 'dog';
	alter table humsters 
		add column type varchar(200) default 'humster';
	alter table horses
		add column type varchar(200) default 'horse';
	alter table camels 
		add column type varchar(200) default 'camel';
        alter table donkies
		add column type varchar(200) default 'donkey';
	select * from cats
    union
    select * from dogs
    union
    select * from humsters;
    select * from horses
    union
    select * from camels 
    union
    select * from donkies;
    
    create table b (
	id int auto_increment primary key,
	name varchar(200),
    birth_date date Not null,
    comands varchar(200),
    type varchar(200)
    );
     insert into b 
     select *from cats 
     where (datediff(curdate(),birth_date)<=365*3);
     insert into b 
     select *from dogs 
     where (datediff(curdate(),birth_date)<=365*3);
     insert into b 
     select *from humsters 
     where (datediff(curdate(),birth_date)<=365*3);
     insert into b 
     select *from horses
     where (datediff(curdate(),birth_date)<=365*3);
     insert into b 
     select *from camels
     where (datediff(curdate(),birth_date)<=365*3);
     insert into b 
     select *from donkies 
     where (datediff(curdate(),birth_date)<=365*3);
     
    alter table b 
		add column age int;
        
	update b set age=extract(month from curdate())- 
    extract(month from birth_date)+
    extract(year from curdate())*12-
    extract(month from birth_date)*12;
    
