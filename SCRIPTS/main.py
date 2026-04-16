import pandas as pd
import numpy as np
import re
import sqlite3

connection = sqlite3.connect("../INPUTS/databse.sqlite")

"""
The database has the following tables:

Player_Attributes
Player
Match
League
Country
Team
Team_Attributes
"""


df_player = pd.read_sql_query("SELECT * FROM Player", connection)
df_player_attributes = pd.read_sql_query("SELECT * FROM Player_Attributes", connection)
df_match = pd.read_sql_query("SELECT * FROM Match", connection)
df_league = pd.read_sql_query("SELECT * FROM League", connection)
df_country = pd.read_sql_query("SELECT * FROM Country", connection)
df_team = pd.read_sql_query("SELECT * FROM Team", connection)
df_team_attributes = pd.read_sql_query("SELECT * FROM Team_Attributes", connection)

connection.close()