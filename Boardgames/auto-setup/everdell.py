# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 11:47:59 2021

@author: HgCNO2
"""
import sqlite3 as sql
import pandas as pd
import streamlit as st

# Set database path
db_path = r'C:/Eric/Coding/Python/Games/Boardgames/auto-setup/gamessqlite.db'

# Create set of game series to select from
series = set()
with sql.connect(db_path) as conn:
    for x in conn.execute('SELECT DISTINCT series FROM games'):
        series.update(x)

#TODO Display series to user in a GUI dropdown to be selected
# print('Select a series:\n-' + '\n-'.join(series))
selected_series = st.selectbox("Please select the game series you're playing", series)

#TODO Show all of the games & expansions for the selected series with on/off toggles
with sql.connect(db_path) as conn:
    games_expansions = pd.read_sql(f"SELECT * FROM games WHERE series='{selected_series}'", conn)
    games_expansions['active'] = False

# Create function to set expansions to active or inactive
def on_off(game):
    game['active'] = not game['active']
    
# TODO Create function to run a setup shuffler
