import numpy as np
from sklearn.preprocessing import scale
from sklearn.cluster import KMeans
import import_data

# normalization
data = import_data.import_data_for_kmeans()
data = scale(data)

kmeans=KMeans(n_clusters=10).fit(data)

#print("Centers of clusters",kmeans.cluster_centers_)

samples = [[-4.82492195,  0.39868205,  0.04708505, -0.39915157, -1.78619041],
 [-4.95757716, -0.33659845,  0.18933952, -0.39915157, -1.78619041],
 [-2.70243868,  0.00653245,  0.04708505, -0.39915157,  0.55985073],
 [ 0.74659665,  0.34966335,  0.41694668, -0.39915157,  0.55985073],
 [ 1.14456226,  0.00653245,  0.04708505, -0.39915157,  0.55985073],
 [ 1.27721747, -0.33659845,  0.18933952, -0.39915157,  0.55985073]]

labels=kmeans.predict(data)	#index of the cluster each sample belongs to

print("LABELS:")
print(np.bincount(labels))

labels_str=" ".join(str(elem) for elem in labels)
with open('player_cluster.txt','w') as f:
    f.write(labels_str)
