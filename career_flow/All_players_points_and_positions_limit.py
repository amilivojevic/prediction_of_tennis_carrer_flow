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

a = int(sys.argv[1])
b = int(sys.argv[2])

#------------------------------------------------------------------------------------------------

params = {'legend.fontsize': 'x-large',
          'figure.figsize': (100, 20),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.xticks(np.arange(dates.date2num(datetime.datetime(1973,1,1,0,0)), dates.date2num(datetime.datetime(2018,1,1,0,0)), 366))

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


k=0

if b> len(players):
	b=len(players)

for playerId in players[a:b]:
	print(playerId,k)
	k=k+1
	datesX=list()
	selectedPlayer=p1[np.where(p1["id"]==playerId)]
	if selectedPlayer.size!=0:
		#print(selectedPlayer.size,playerId)
		for n in range(0,np.size(selectedPlayer["y"])):
			datesX.append(datetime.datetime(selectedPlayer["y"][n],selectedPlayer["m"][n],selectedPlayer["d"][n],0,0))
		#print(type(datesX))
		datesX = dates.date2num(datesX)
		
		fig1=plt.figure()
		ax1 = fig1.add_subplot(111)
		ax1.plot_date(datesX, selectedPlayer["ranknum"])
		fig1.savefig('playerFig/'+playerId+'.png')
		plt.close(fig1)

'''
#plt.plot_date(datesX, b028["points"])
#ili:
plt.plot_date(datesX, b028["ranknum"])

svr_rbf = SVR(kernel='rbf', C=150, gamma=0.1)
ry=p1["ranknum"]
svr_rbf.fit(datesX.reshape(-1,1), b028["ranknum"])

x_test = np.linspace(min(datesX),max(datesX))
y_rbf = svr_rbf.predict(x_test[:,None])
plt.plot(x_test, y_rbf, color='navy', label='RBF model')

#print(p1)
#plt.show()
plt.savefig('figures/fig.png')
#plt.savefig('figures/rankings.pdf')
'''