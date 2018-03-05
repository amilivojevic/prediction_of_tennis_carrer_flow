import pandas as pd
import utils

def import_and_clean_data_set():

    # Load in the data with `read_csv()`
    players = pd.read_csv("https://raw.githubusercontent.com/serve-and-volley/atp-world-tour-tennis-data/master/csv/5_players/player_overviews_UNINDEXED.csv",
                          header=None).fillna(0)

    # Set column names (header)
    players.columns = ["player_id","player_slug","first_name","last_name","player_url","flag_code",
                       "residence","birthplace","birthdate", "birth_year","birth_month","birth_day",
                       "turned_pro","weight_lbs","weight_kg","height_ft","height_inches","height_cm",
                       "handedness","backhand"]

    keep_columns = ["player_id","player_slug","flag_code",
                       "residence","birthplace","birthdate",
                       "turned_pro","weight_kg","height_cm",
                       "handedness","backhand"]

    players = players[keep_columns]

    # change type of columns
    players['birthdate'] = pd.to_datetime(players["birthdate"],format= "%Y.%m.%d")
    # players['turned_pro'] = pd.to_datetime(players["turned_pro"],format= "%Y.0")
    players['turned_pro'] = players.turned_pro.astype(int)

    # Print out
    # print(players.head())

    for col in players.columns:
        print('column', col,':', type(players[col][0]))

    # quick statistic summary of players data
    print(players.describe())

    utils.turnedProMissingValues(players)
    # handednessCountMissingValues()
    players = utils.handednessDropRowsWithMissingValues(players)
    players = utils.weightMissingValues(players)
    utils.backhandToInt(players)
    utils.handednessToInt(players)
    print("*****")
    print("players size: ", len(players))
    print(players.head())
    return players

def import_data_for_kmeans():
    players = import_and_clean_data_set()
    # keep_columns = [ "birthdate","turned_pro", "weight_kg", "height_cm","handedness", "backhand"]
    keep_columns = [ "turned_pro", "weight_kg", "height_cm", "handedness", "backhand"]

    return players[keep_columns]
