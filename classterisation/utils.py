def avgTurnedPro(players):
    counter = 0
    sum = 0

    for ind,player in players.iterrows():
        if (player["birthdate"].year >0 and player['turned_pro'] != 0):
            years = player['turned_pro'] - player["birthdate"].year
            # print("years: ", years)
            if (years < 10):
                print("outliers: ", years)
            else:
                sum += years
                counter += 1

    avg = sum/counter
    print("AVG years turning pro: %f",avg)
    return avg

def turnedProMissingValues(players):
    avg = avgTurnedPro(players)
    indecies = []
    for ind,player in players.iterrows():
        if (player['turned_pro'] == 0):
            indecies.append(ind)
            players.at[ind,"turned_pro"] = player['birthdate'].year + avg

    '''
    for i in indecies:
        print(players.iloc[[i]]['turned_pro'])
    '''

def handednessToInt(players):
    print(players['handedness'].head())
    for ind,player in players.iterrows():
        if (player['handedness'] == "Right-Handed"):
            players.at[ind, "handedness"] = 1
        if (player['handedness'] == "Left-Handed"):
            players.at[ind, "handedness"] = 2
        if (player['handedness'] == "Ambidextrous"):
            players.at[ind, "handedness"] = 3

def backhandToInt(players):
    for ind,player in players.iterrows():
        if (player['backhand'] == "One-Handed Backhand"):
            players.at[ind, "backhand"] = 1
        if (player['backhand'] == "Two-Handed Backhand"):
            players.at[ind, "backhand"] = 2

def handednessCountMissingValues(players):
    count =0
    count1 = 0
    count2 = 0
    for ind,player in players.iterrows():
        if (player['handedness'] == 0):
            count += 1
        if (player['handedness'] == "Right-Handed"):
            count1 += 1
        if (player['handedness'] == "Left-Handed"):
            count2 += 1
    print("Handedness missing value: ", count)
    print("Handedness missing value COUNT1: ", count1)
    print("Handedness missing value COUNT2: ", count2)

def handednessDropRowsWithMissingValues(players):
    indexes = []
    for ind,player in players.iterrows():
        if (player['handedness'] == 0):
            indexes.append(ind)

    return players.drop(indexes)

def weightMissingValues(players):
    indexes = []
    for ind, player in players.iterrows():
        if (player['weight_kg'] == 0):
            indexes.append(ind)

    return players.drop(indexes)

