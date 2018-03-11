# Import matplotlib
import matplotlib.pyplot as plt
import import_data

players = import_data.import_data_for_kmeans()

weights = players["weight_kg"]

heights = players["height_cm"]

plt.scatter(range(len(weights)), weights, color='darkgreen', marker='^')
plt.scatter(range(len(heights)), heights, color='red', marker='.')
plt.ylim(50, 700)
plt.show()
