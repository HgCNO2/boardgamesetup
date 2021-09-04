import streamlit as st
import pandas as pd
import sqlite3 as sql
import random

db_path = st.secrets['sqlite']


def run(game_series='Robinson Crusoe'):
    selected_series = game_series

    # Pull data for games & expansions
    with sql.connect(**db_path) as conn:
        games_expansions = pd.read_sql(f"SELECT * FROM games WHERE series='{selected_series}'", conn)
    games_expansions.sort_values('game_name', inplace=True)

    # Show all of the games & expansions for the selected series with on/off toggles
    selected_games = st.multiselect('Which games and expansions are you playing today?',
                                    games_expansions['game_name'],
                                    default='Robinson Crusoe: Adventures on the Cursed Island'
                                    )

    # Get number of players
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

    # Shuffle Characters
    if num_players == 4:
        characters = shuffler('Character', num_players)
    else:
        incl_soldier = st.checkbox('Include Soldier?')
        if incl_soldier:
            characters = shuffler('Character', num_players)
        else:
            characters = shuffler('Character', 4)
            try:
                characters.remove('Soldier')
                characters = random.sample(characters, num_players)
            except ValueError:
                characters = random.sample(characters, num_players)

    # Shuffle Starting Equipment
    starting_equipment = shuffler('Starting Equipment', 2)

    # Shuffle Inventions
    default_inventions = list(component_table[component_table['comp_type'] == 'Default Invention']['comp_name'])

    inventions = list(component_table[component_table['comp_type'] == 'Invention']['comp_name'])

    character_inventions = {'Carpenter': 'Snare',
                            'Cook': 'Fireplace',
                            'Explorer': 'Shortcut',
                            'Soldier': 'Spear',
                            'Sailor': 'Raft'}

    for character in characters:
        inventions.remove(character_inventions[character])

    inventions = random.sample(inventions, 5)
    inventions.append(default_inventions)

    # Create button to run the setup
    with st.form(key='my_form'):
        submit_button = st.form_submit_button(label='Run Game Setup')

    player = 1
    character_string = '**Your character assignments are:**'
    for character in characters:
        character_string += f'  \nPlayer {player}: {character}'
        player += 1

    starting_equipment_string = '**Your Starting Equipment is:**'
    for equipment in starting_equipment:
        starting_equipment_string += f'  \n| {equipment} |'

    invention_string = '**Your Inventions are:**'
    for invention in inventions:
        invention_string += f'  \n| {invention} |'

    if submit_button:
        st.markdown(character_string)
        st.markdown(starting_equipment_string)
        st.markdown(invention_string)


if __name__ == '__main__':
    run()
