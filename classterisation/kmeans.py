import numpy as np
from sklearn.preprocessing import scale
from sklearn.cluster import KMeans
import import_data

# normalization
data = import_data.import_data_for_kmeans()
data = scale(data)

n_clusters=10;
kmeans=KMeans(n_clusters=10).fit(data)

labels=kmeans.predict(data)	#index of the cluster each sample belongs to

id_index={}
id_index=import_data.playerId_index()

for k in range(0,n_clusters):
	temp="labels_str"+str(k);  
	locals()[temp]=""
	
i=0;
for index in labels:
	for k in range(0,n_clusters):
		if index==k:
			locals()["labels_str"+str(k)]+=id_index[i]+" ";
	i+=1;

for k in range(0,n_clusters):
	with open('player_cluster'+str(k)+'.txt','w') as f:
		f.write(locals()["labels_str"+str(k)])

print("LABELS:")
print(np.bincount(labels))

