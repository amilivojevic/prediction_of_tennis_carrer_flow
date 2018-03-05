from sklearn.preprocessing import scale
from sklearn.cluster import KMeans
import import_data
# Import `train_test_split`
from sklearn.cross_validation import train_test_split

# normalization
data = import_data.import_data_for_kmeans()
data = scale(data)
# print(data)
