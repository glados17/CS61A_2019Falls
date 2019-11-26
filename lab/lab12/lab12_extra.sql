.read lab12.sql

CREATE TABLE smallest_int_having AS
  SELECT time, smallest
  from students
  group by smallest
  having count(*) = 1
  order by smallest;

CREATE TABLE fa19favpets AS
  SELECT pet,count(*) as counts
  from students
  group by pet
  order by counts desc, pet
  limit 10;


CREATE TABLE fa19dog AS
  SELECT pet, count(*) as counts
  from students
  group by pet
  having pet = 'dog';


CREATE TABLE obedienceimages AS
  SELECT seven, instructor, count(*) as counts
  from students
  where seven = '7'
  group by instructor;
  
