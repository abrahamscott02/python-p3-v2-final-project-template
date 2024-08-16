import sqlite3

CONN = sqlite3.connect('roster.db')
CURSOR = CONN.cursor()
