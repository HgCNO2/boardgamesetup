# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 11:47:59 2021

@author: HgCNO2
"""
import sqlite3 as sql
import pandas as pd
import streamlit as st
import random

st.set_page_config('Everdell Automatic Game Setup by HgCNO2')

# Set database path
db_path = r'C:/Eric/Coding/Python/Games/Boardgames/auto-setup/gamessqlite.db'

# Create set of game series to select from
series = set()
with sql.connect(db_path) as conn:
    for x in conn.execute('SELECT DISTINCT series FROM games'):
        series.update(x)

# Display series to user in a GUI dropdown to be selected
selected_series = st.selectbox("Please select the game series you're playing", series)

# Pull data for games & expansions 
with sql.connect(db_path) as conn:
    games_expansions = pd.read_sql(f"SELECT * FROM games WHERE series='{selected_series}'", conn)

# Show all of the games & expansions for the selected series with on/off toggles
selected_games = st.multiselect('Which games and expansions are you playing today?', games_expansions['game_name'], default='Everdell')

# Get number of players
if 'Bellfaire' in selected_games:
    num_players = st.selectbox("How many players are playing?", range(1,7))
else:
    num_players = st.selectbox("How many players are playing?", range(1,5))

# Build SQL call for just the selected games
joined_call = r"SELECT * FROM games JOIN components ON games.id=components.game_id WHERE "
for game in selected_games:
    if game != selected_games[-1]:
        joined_call += f'games.game_name="{game}" OR '
    else:
        joined_call += f'games.game_name="{game}"'
        
# Join tables to add all of the components for the selected games
with sql.connect(db_path) as conn: 
    component_table = pd.read_sql(joined_call, conn)

# Run the setup shuffler
## Workers
workers = random.sample(list(component_table[component_table['comp_type'] == 'Worker']['comp_name']), num_players)

## Special Events
if num_players == 6:
    special_events = random.sample(list(component_table[component_table['comp_type'] == 'Special Event']['comp_name']), num_players)
elif num_players == 5:
    special_events = random.sample(list(component_table[component_table['comp_type'] == 'Special Event']['comp_name']), num_players)
else:
    special_events = random.sample(list(component_table[component_table['comp_type'] == 'Special Event']['comp_name']), 4)

## Forest Locations
if num_players <= 2:
    forest_locations = random.sample(list(component_table[component_table['comp_type'] == 'Forest Location']['comp_name']), 3)
else:
    forest_locations = random.sample(list(component_table[component_table['comp_type'] == 'Forest Location']['comp_name']), 4)
    
# Create button to run the setup
with st.form(key='my_form'):
	submit_button = st.form_submit_button(label='Run Game Setup')
    
player = 1
worker_string = '**Your workers are:**'
for worker in workers:
    worker_string += f'  \nPlayer {player}: {worker}'
    player += 1

forest_string = '**Your Forest Locations are:**'
for location in forest_locations:
    forest_string += f'  \n| {location} |'
        
event_string = '**Your Special Events are:**'
for event in special_events:
    event_string += f'  \n| {event} |'


if submit_button:
    st.markdown(worker_string)
    st.markdown(forest_string)
    st.markdown(event_string)