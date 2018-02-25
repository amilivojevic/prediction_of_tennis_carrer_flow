from matplotlib import pyplot as plt
import numpy as np
from matplotlib import style
from operator import itemgetter, attrgetter
from matplotlib import dates
import datetime
import urllib.request
import matplotlib.pylab as pylab
from sklearn.svm import SVR
import pandas as pd
import sys

from sklearn.preprocessing import MinMaxScaler

#------------------------------------------------------------------------------------------------

params = {'legend.fontsize': 'x-large',
          'figure.figsize': (100, 20),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.xticks(np.arange(0,1.2,0.2))

style.use('ggplot')


#--------------------------------------------------------------------------------------------------

#prvi dataset - 1973
url = "https://raw.githubusercontent.com/serve-and-volley/atp-world-tour-tennis-data/master/csv/4_rankings/rankings_1973.csv"
raw_data = urllib.request.urlopen(url)
p1=np.genfromtxt(url,dtype=["U12","i2","i2","i2","i2","i2","i2","U4","i2","i2","i2","U100","U50","U4"], names=["week","y","m","d","ranktxt","ranknum","move_pos","move_dir","player_age","points","tourneys","url","slug","id"],delimiter=',')

players = pd.read_csv("https://raw.githubusercontent.com/serve-and-volley/atp-world-tour-tennis-data/master/csv/5_players/player_overviews_UNINDEXED.csv", header=None)
#players=np.genfromtxt(url2,dtype=["U12","U20","U20","U20","U100","U5","U20","U20","U20","i4","i2","i2","i4","i4","i4","U10","i4","i4","U10","U10"], names=["id","slug","name","first_name","last_name","url","flag","residence","birthdate","birth_year","birth_month","birth_day","turned_pro","weight_lbs","weight_kg","height_ft","height_inches","height_cm","handedness","backhand"],delimiter=',')
players=players.iloc[:,0]

p1.sort(order = ("y","m","d"))


#---------------------------------------------------------------------------------------------------
#ostali: 1974 - 2017
#Memory error: moguce da zahteva 64bit

for n in range(1974,2018):
	url = "https://raw.githubusercontent.com/serve-and-volley/atp-world-tour-tennis-data/master/csv/4_rankings/rankings_"+str(n)+".csv"
	raw_data = urllib.request.urlopen(url)
	p2=np.genfromtxt(url,dtype=["U12","i2","i2","i2","i2","i2","i2","U4","i2","i2","i2","U100","U50","U4"], names=["week","y","m","d","ranktxt","ranknum","move_pos","move_dir","player_age","points","tourneys","url","slug","id"],delimiter=',')
	print(n)
	p2.sort(order = ("y","m","d"))
	p1=np.append(p1,p2,axis=0)

#---------------------------------------------------------------------------------------------------


def getPlayer(playerID):
	dates_list=list()

	player=p1[np.where(p1["id"]==playerID)]
	player_rank=player["ranknum"]

	scaler = MinMaxScaler()
	scaler.fit(player_rank.reshape(-1,1))
	player_rank_norm=1-scaler.transform(player_rank.reshape(-1,1))

	for n in range(0,np.size(player["y"])):
		dates_list.append((datetime.datetime(player["y"][n],player["m"][n],player["d"][n],0,0)-datetime.datetime(1970,1,1)).days)

	datesX=np.array(dates_list)

	scaler2 = MinMaxScaler()
	scaler2.fit(datesX.reshape(-1,1))
	dates_norm=scaler2.transform(datesX.reshape(-1,1))

	return np.concatenate((dates_norm, player_rank_norm), axis=1)

#--------------------------------------------------------------------------------------------------	


del sys.argv[0]
first=sys.argv.pop(0)
print(first)
xy=getPlayer(first)

for player in sys.argv:
	print(player)
	playerData=getPlayer(player)
	xy=np.append(xy,playerData,axis=0)

xy_sorted = np.core.records.fromarrays(xy.transpose(), names='x,y', formats = 'f8, f8')

xy_sorted.sort(order = "x")


svr_rbf = SVR(kernel='rbf', C=1e3, gamma=10)

svr_rbf.fit(xy_sorted["x"].reshape(-1,1), xy_sorted["y"])

x_test = np.linspace(min(xy_sorted["x"]),max(xy_sorted["x"]))
y_rbf = svr_rbf.predict(x_test[:,None])
plt.plot(x_test, y_rbf, color='red', label='RBF model')

plt.plot(xy_sorted['x'],xy_sorted['y'], marker='o', linestyle='None')
plt.savefig('normalized/rankings.png')

#print(xy_sorted)




