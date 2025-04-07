-- 01. Querying data
SELECT 
  LastName
FROM
  employees;

SELECT LastName,FirstName FROM employees;

SELECT * FROM employees;

SELECT FirstName AS "이름" FROM employees;

SELECT Name, 
  Milliseconds/60000 as '재생 시간(분)' 
FROM
  tracks;

-- 02. Sorting data
SELECT 
  FirstName
FROM
  employees
ORDER BY
  FirstName;

SELECT 
  FirstName
FROM
  employees
ORDER BY
  FirstName DESC;

SELECT
  Country, City
FROM
  customers
ORDER BY
  Country DESC,
  City;

SELECT Name, Milliseconds/60000 as '재생시간(분)' FROM tracks ORDER BY Milliseconds DESC;

-- NULL 정렬 예시
SELECT 
  postalCode
FROM
  customers
ORDER BY
  postalCode;

-- 03. Filtering data
SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;

SELECT LastName, FirstName, City from customers where "City" != 'Prague';
SELECT LastName, FirstName, Company, Country FROM customers where "Company" IS Null and Country = 'USA';
SELECT  LastName, FirstName, Company, Country FROM customers where "Company" IS Null OR Country = 'USA';

SELECT NAME, BYTES FROM tracks WHERE "Bytes" BETWEEN 100000 AND 500000;
SELECT "Name", BYTES FROM tracks WHERE "Bytes" BETWEEN 100000 AND 500000
ORDER BY "Bytes";
SELECT "Name", BYTES FROM tracks WHERE "Bytes" >= 100000 AND "Bytes" <= 500000;

SELECT LASTNAME, FIRSTNAME, COUNTRY FROM customers WHERE COUNTrY = 'Canada' or country ='Germany' or "Country" = 'France';
SELECT LASTNAME, FIRSTNAME, COUNTRY FROM customers WHERE COUNTrY in ('Canada','Germany','France');
SELECT LASTNAME, FIRSTNAME, COUNTRY FROM customers WHERE COUNTrY not in ('Canada','Germany','France');

SELECT lastname, firstname from customers where "LastName" like '%son';
SELECT lastname, firstname FROM customers where "FirstName" like '___a';

# LIMIT
SELECT TRACKID, NAME, BYTES FROM TRACKS  ORDER BY "Bytes" DESC LIMIT 7;
SELECT TRACKID, NAME, BYTES FROM TRACKS  ORDER BY "Bytes" DESC LIMIT 3,4;
SELECT TRACKID, NAME, BYTES FROM TRACKS  ORDER BY "Bytes" DESC LIMIT 4 OFFSET 3;

-- 04. Grouping data
SELECT
  Country, count(*)
FROM
  customers
GROUP BY
  Country;

select composer, 
AVG(bytes) AS avgOfBytes from tracks GROUP BY "Composer" ORDER BY avgOfBytes DESC;

