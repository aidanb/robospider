CREATE TABLE sites (
	id 	INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	url 	VARCHAR(50) UNIQUE,
	crawled	DATE,
	robots 	VARCHAR(10000)
);

-- URL
-- is of the form www.something.com.au
-- any number of domains are allowed
-- no http:// and no trailing slashes!

-- CRAWLED
--  refers to the date crawled, not the date added

-- ROBOTS
--  the robots.txt unedited text
