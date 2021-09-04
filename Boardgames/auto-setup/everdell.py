# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 11:47:59 2021

@author: HgCNO2
"""
import sqlite3 as sql
import pandas as pd
import streamlit as st
import random
import importlib

st.set_page_config('Everdell Automatic Game Setup by HgCNO2', page_icon="https://cf.geekdo-static.com/mbs/mb_43422_0.png")

# Set database path
db_path = st.secrets['sqlite']

# Create list of game series to select from
series = []
with sql.connect(**db_path) as conn:
    for x in conn.execute('SELECT DISTINCT series FROM games'):
        series.append(x[0])
series.sort()

# Display series to user in a GUI dropdown to be selected
selected_series = st.selectbox("Please select the game series you're playing", series)

game = importlib.import_module(selected_series.strip())

game.test()

# Pull data for games & expansions
with sql.connect(**db_path) as conn:
    games_expansions = pd.read_sql(f"SELECT * FROM games WHERE series='{selected_series}'", conn)
games_expansions.sort_values('game_name', inplace=True)

# Show all of the games & expansions for the selected series with on/off toggles
selected_games = st.multiselect('Which games and expansions are you playing today?',
                                games_expansions['game_name'],
                                default='Everdell')

# Get number of players
if 'Bellfaire' in selected_games:
    num_players = st.selectbox("How many players are playing?", range(1, 7))
else:
    num_players = st.selectbox("How many players are playing?", range(1, 5))

# Build SQL call for just the selected games
joined_call = r"SELECT * FROM games JOIN components ON games.id=components.game_id WHERE "
for game in selected_games:
    if game != selected_games[-1]:
        joined_call += f'games.game_name="{game}" OR '
    else:
        joined_call += f'games.game_name="{game}"'

# Join tables to add all of the components for the selected games
with sql.connect(**db_path) as conn:
    component_table = pd.read_sql(joined_call, conn)


# Create shuffler function
def shuffler(component_type, cards_to_deal):
    return random.sample(list(component_table[component_table['comp_type'] == component_type]['comp_name']),
                         cards_to_deal)


# Shuffle Workers
workers = shuffler('Worker', num_players)

# Shuffle Special Events
if num_players == 6:
    special_events = shuffler('Special Event', 6)
elif num_players == 5:
    special_events = shuffler('Special Event', 5)
else:
    special_events = shuffler('Special Event', 4)

# Shuffle Forest Locations
if num_players <= 2:
    forest_locations = shuffler('Forest Location', 3)
else:
    forest_locations = shuffler('Forest Location', 4)

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