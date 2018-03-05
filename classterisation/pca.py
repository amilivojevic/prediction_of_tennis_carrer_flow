import import_data
from sklearn import decomposition

players = import_data.import_and_clean_data_set()

# Create a regular PCA model
pca = decomposition.PCA(n_components=2)

# Fit and transform the data to the model
reduced_data_pca = pca.fit_transform(players)

# Inspect the shape
reduced_data_pca.shape

# Print out the data
print(reduced_data_pca)