-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


--create tournament database
CREATE DATABASE tournament;

\c tournament

--create players table
CREATE TABLE players (
	id serial primary key,
	name text
);

--create matches table, results 1-winner, 0 loser
CREATE TABLE matches (
	id integer references players,
	result real
);

CREATE VIEW standings as
	select players.id, players.name, coalesce(sum(matches.result), 0) as wins, count(matches.result)
	from players left join matches
	on players.id = matches.id
	group by players.id
	order by wins desc;

