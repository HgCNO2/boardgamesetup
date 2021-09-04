# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 11:47:59 2021

@author: HgCNO2
"""
import sqlite3 as sql
import streamlit as st
import importlib

st.set_page_config('Automatically Setup Your Boardgames | HgCNO2 Short Automaton',
                   page_icon="https://cf.geekdo-static.com/mbs/mb_5834_0.gif")

# Set database path
db_path = st.secrets['sqlite']

# Write Header for section
st.header('Choose your adventure.', anchor=None)

# Create list of game series to select from
series = []
with sql.connect(**db_path) as conn:
    for x in conn.execute('SELECT DISTINCT series FROM games'):
        series.append(x[0])
series.sort()

# Display series to user in a GUI dropdown to be selected
selected_series = st.selectbox("Please select the game series you're playing", series)
game = importlib.import_module(selected_series.lower().replace(' ', '_'))

# Headline for the game series
st.header(f'Set up your game of {game_series}', anchor=None)

game.run(selected_series)