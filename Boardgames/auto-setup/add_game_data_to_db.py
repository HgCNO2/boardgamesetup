# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 21:47:42 2021

@author: HgCNO2
"""
import sqlite3 as sql
import pandas as pd

db_path = r'gamessqlite.db'

games = {'game_name':['Everdell', "Everdell Collector's Edition", 'Pearlbrook', 
         "Pearlbrook Collector's Edition", 'Bellfaire', 'Spirecrest',
         "Spirecrest Collector's Edition", 'Newleaf', 'Mistwood']}

games_df = pd.DataFrame(games)

games_df['series'] = 'Everdell'
games_df['id'] = range(1,10)

with sql.connect(db_path) as conn:
    # games_df.to_sql('games', conn, index=False, if_exists='append')
    games_df_2 = pd.read_sql('SELECT * FROM games', conn)

everdell_components = {'comp_name':['Cardinals', 'Toads',
                                    '3 Resin', '2 Resin or 2 Berries',
                                    'Pay 3 Twigs, Get 3 of any resource',
                                    'Activate 2 Green Production in your city',
                                    'City Holiday', 'Bed & Breakfast Guide', 'Gathering of Elders',
                                    'Architectural Renaissance', 'Arts & Music Festival',
                                    'Pie Eating Contest', "King's Road Established",
                                    'Statues Commissioned', 'Royal Wedding'],
                       'comp_type':['Workers', 'Workers',
                                    'Forest Location', 'Forest Location', 'Forest Location', 'Forest Location',
                                    'Special Event',
                                     'Special Event',
                                     'Special Event',
                                     'Special Event',
                                     'Special Event',
                                     'Special Event',
                                     'Special Event',
                                     'Special Event',
                                     'Special Event']}

components_df = pd.DataFrame(everdell_components)
components_df['game_id'] = 6
components_df['comp_id'] = range(63)

# with sql.connect(db_path) as conn:
#     components_df.to_sql('components', conn, index=False, if_exists='append')