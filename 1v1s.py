from multielo import MultiElo, Player, Tracker
import pandas as pd
import numpy as np
from datetime import datetime
import pickle
import os

# read the history from pickle if it exists, otherwise create a new tracker
try:
    # get current directory
    curr_dir = os.getcwd()

    # load the player data
    file = os.path.join(curr_dir, "ones_rankings.pickle")
    tracker = Tracker(players=file)
except FileNotFoundError:
    # create a new tracker
    tracker = Tracker()

# print the current ratings
print("Current Ratings:")
print(tracker.get_current_ratings())

def add_game():
    # get the winner and loser
    players = input("Enter players in winning order: ").split(' ')

    # turn input into dataframe
    curr_date = datetime.now().strftime("%Y-%m-%d")

    data = pd.DataFrame({
        "date": [curr_date],
        "1st": [players[0]],
        "2nd": [players[1]],
    })

    # add the game to the tracker
    tracker.process_data(data)
    
    # get current directory
    curr_dir = os.getcwd()

    # save the player data
    file = os.path.join(curr_dir, "ones_rankings.pickle")
    tracker.save_player_data(file, save_full_history=True)


# add a game
while True:
    add_game()
    print("Current Ratings:")
    print(tracker.get_current_ratings())
    if input("Add another game? (y/n): ") != 'y':
        break