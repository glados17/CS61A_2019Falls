CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size
    from dogs, Sizes
    where dogs.height > sizes.min and dogs.height <= sizes.max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT parents.child
    from dogs, parents
    where dogs.name = parents.parent
    order by dogs.height desc;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.name as name1, b.name as name2, a.size as size
  from size_of_dogs as a, size_of_dogs as b, parents as c, parents as d
    where a.name = c.child and a.size = b.size and
      b.name = d.child and c.parent = d.parent and a.name < b.name
    order by a.size;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT name1 || ' and ' || name2 || ' are '|| size || ' siblings' from siblings;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);

INSERT into stacks_helper
  select name, height, height from dogs
  order by height;

insert into stacks_helper
  select dogs.name || ', ' ||stacks_helper.dogs, 
    dogs.height + stacks_helper.stack_height, dogs.height from dogs, stacks_helper
  where stacks_helper.last_height > dogs.height;

insert into stacks_helper
  select dogs.name || ', ' ||stacks_helper.dogs, 
    dogs.height + stacks_helper.stack_height, dogs.height from dogs, stacks_helper
  where stacks_helper.last_height > dogs.height;

insert into stacks_helper
  select dogs.name || ', ' ||stacks_helper.dogs, 
    dogs.height + stacks_helper.stack_height, dogs.height from dogs, stacks_helper
  where stacks_helper.last_height > dogs.height;
-- Add your INSERT INTOs here


CREATE TABLE stacks AS
  SELECT dogs, stack_height from  stacks_helper
  where stack_height > 170
  order by stack_height;
