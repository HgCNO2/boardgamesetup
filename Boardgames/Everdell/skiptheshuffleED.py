## Program to set up Everdell without shuffling
import random

# List of All Everdell Base Forest Locations
allForest = ['Copy any basic action on the board & 1 card', 'Discard any resource, then Draw 2 for every card discarded', 'Discard up to 3 cards & gain 1 of any resource for each card', 'Draw 2 Meadow cards & play 1 for -1 of any resource', '1 Twig, 1 Resin, 1 Berry', '3 Berries', '3 Cards & 1 Pebble', '2 of Any Resource', '2 Berries & 1 Card', '2 Cards & 1 of Any Resource', '2 Resin & 1 Twig']

# List of All Everdell Base Special Events
allSpecEvent = ['Remembering the Fallen', 'A Well Run City', 'Capture of the Acorn Thieves', 'Flying Doctor Service', 'Ancient Scrolls Discovered', 'Performer in Residence', 'Tax Relief', 'Path of the Pilgrims', 'Ministering to Miscreants', 'Under New Management', 'A Brilliant Marketing Plan', 'Graduation of Scholars', 'An Evening of Fireworks', 'The Everdell Games', 'Croak Wart Cure', 'Pristine Chapel Ceiling']

# Empty List for Selected Forest Locations
setupForest = []

# Empty list for Selected Special Events
setupSpecEvent = []

# Prompt Number of Players
numPlayers = int(input('How many players are playing? 1, 2, 3, or 4?\n'))

# Randomly Generate Forest Locations
if numPlayers <=2:
    setupForest = random.sample(allForest, k=3)
else:
    setupForest = random.sample(allForest, k=4)
print('\nYour forest locations are: \n--' + '\n--'.join(setupForest))
    
# Randomly Generate Special Events
setupSpecEvent = random.sample(allSpecEvent, k=4)
print('\nYour special events are: \n--' + '\n--'.join(setupSpecEvent))
input('\nEnjoy the game!\nPress ENTER to exit.')
