# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 11:47:59 2021

@author: HgCNO2
"""

# Create data for games
everdell = {'active':True,
            'workers':['Mice', 'Squirrels', 'Hedgehogs', 'Turtles'],
            'forest locations':['Copy any basic action on the board & 1 card',
                                'Discard any resource, then Draw 2 for every card discarded',
                                'Discard up to 3 cards & gain 1 of any resource for each card',
                                'Draw 2 Meadow cards & play 1 for -1 of any resource',
                                '1 Twig, 1 Resin, 1 Berry', '3 Berries',
                                '3 Cards & 1 Pebble', '2 of Any Resource',
                                '2 Berries & 1 Card', '2 Cards & 1 of Any Resource',
                                '2 Resin & 1 Twig'],
            'special events':['Remembering the Fallen', 'A Well Run City',
                              'Capture of the Acorn Thieves', 'Flying Doctor Service',
                              'Ancient Scrolls Discovered', 'Performer in Residence',
                              'Tax Relief', 'Path of the Pilgrims',
                              'Ministering to Miscreants', 'Under New Management',
                              'A Brilliant Marketing Plan', 'Graduation of Scholars',
                              'An Evening of Fireworks', 'The Everdell Games',
                              'Croak Wart Cure', 'Pristine Chapel Ceiling']}

everdell_collectors_edition = {'active':False,
                               'workers':['Rats'],
                               'forest locations':None,
                               'special events':None}

pearlbrook = {'active':False,
              'workers':['Otters'],
              'forest locations':[],
              'special events':[]}

pearlbrook_collectors_edition = {'active':False,
                                 'workers':['Otters', 'Axolotls', 'Platypus', 'Starlings'],
                                 'forest locations':['1 Berry, 1 Pebble, 1 Card',
                                                     '2 Pebbles, 1 Card',
                                                     '1 Resin, 1 Pebble, 4 Cards',
                                                     'Discard 2 Meadow cards, replenish, then draw 2 Meadow cards, also gain 1 of Any resource'],
                                 'special events':['Mascquerade Invitations',
                                                   'River Race', 'Riverside Resort',
                                                   'Romantic Cruise', 'X Marks the Spot',
                                                   'Sunken Treasure Discovered']}

bellfaire = {'active':False,
             'workers':['Cardinals', 'Toads'],
             'forest locations':['3 Resin', '2 Resin or 2 Berries',
                                  'Pay 3 Twigs, Get 3 of any resource',
                                  'Activate 2 Green Production in your city'],
             'special events':['City Holiday', 'Bed & Breakfast Guide', 'Gathering of Elders',
                                'Architectural Renaissance', 'Arts & Music Festival',
                                'Pie Eating Contest', "King's Road Established",
                                'Statues Commissioned', 'Royal Wedding']}

spirecrest = {'active':False,
              'workers':['Foxes'],
              'forest locations':[],
              'special events':[]}

spirecrest_collectors_edition = {'active':False,
                                 'workers':['Owls', 'Lizard', 'Moles'],
                                 'forest locations':[],
                                 'special events':[]}

# Create function to set expansions to active or inactive
def on_off(game):
    game['active'] = not game['active']
    
# Setting up sqlite database
import sqlite3

db_path = r'gamessqlite.db'

create_games_table = '''CREATE TABLE games(
                        id INTEGER PRIMARY KEY,
                        series text,
                        game_name text
                        )'''

create_components_table = '''CREATE TABLE components(
                        id INTEGER PRIMARY KEY,
                        component_name text,
                        type text,
                        FOREIGN KEY (id) REFERENCES games (game_id)
                        )'''
    
with sqlite3.connect(db_path) as connection:
    cursor = connection.cursor()
    # cursor.execute('DROP TABLE components')
    # cursor.execute('DROP TABLE games')
    # cursor.execute(create_games_table)
    cursor.execute(create_components_table)
        


















