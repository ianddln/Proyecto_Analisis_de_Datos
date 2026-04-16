import pandas as pd
import sqlite3

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("../INPUTS/database.sqlite")

cur = con.cursor()

# Query to get all table names
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()

# tables is a list of tuples: [('table1',), ('table2',)]
for table in tables:
    print(table[0])