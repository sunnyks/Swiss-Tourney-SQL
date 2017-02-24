#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
	db = connect()
	c = db.cursor()
	c.execute("delete from matches;")
	db.commit()
	db.close()


def deletePlayers():
	db = connect()
	c = db.cursor()
	c.execute("delete from players;")
	db.commit()
	db.close()


def countPlayers():
	db = connect()
	c = db.cursor()
	c.execute("select count(*) from players;")
	result = c.fetchone()[0]
	db.close()
	return result


def registerPlayer(name):
	db = connect()
	c = db.cursor()
	c.execute("insert into players (name) values (%s);", (name,))
	db.commit()
	db.close()


def playerStandings():
	db = connect()
	c = db.cursor()
	c.execute("select * from standings;")
	result = c.fetchall()
	db.close()
	return result


def reportMatch(winner, loser):
	db = connect()
	c = db.cursor()
	c.execute("insert into matches (id, result) values (%s, 1);", (winner,))
	c.execute("insert into matches (id, result) values (%s, 0);", (loser,))
	db.commit()
	db.close()
	
 
 
def swissPairings():
	standings = playerStandings()
	return [(standings[i-1][0], standings[i-1][1], standings[i][0], standings[i][1])
		for i in range(1, len(standings), 2)]


