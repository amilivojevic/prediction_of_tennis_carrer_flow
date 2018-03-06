from sklearn.preprocessing import scale
from sklearn.cluster import KMeans
import import_data
# Import `train_test_split`
from sklearn.cross_validation import train_test_split

# normalization
data = import_data.import_data_for_kmeans()
data = scale(data)

print("Size of data:",data.size)

kmeans=KMeans(n_clusters=5,max_iter=50).fit(data)
labels=kmeans.predict(data)	#index of the cluster each sample belongs to
print("Size of leng labels:",labels.size)

num_clus=[0, 0, 0, 0, 0]
for i in labels:
	num_clus[labels[i]]+=1

for i in range(5):
	print("Cluster",i,"has", num_clus[i],"items")
