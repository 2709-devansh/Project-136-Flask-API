import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import pandas as pd

df = pd.read_csv("Stars-Gravity.csv")
radius = df["Radius"]
mass = df["Mass"]

X = []
for index, planet_mass in enumerate(mass):
    temp_list = [radius[index], planet_mass]
    X.append(temp_list)

kValues = []

for i in range(1, 11):
    kMeans = KMeans(n_clusters = i, init = "k-means++", random_state = 42)
    kMeans.fit(X)
    kValues.append(kMeans.inertia_)

plt.figure(figsize = (20,10))
sns.lineplot(range(1,11), kValues, markers = 'o', color = "red")
plt.xlabel("Number of Clusters")
plt.show()

k_means = KMeans(n_clusters = 5, init = "k-means++", random_state = 42)
prediction = k_means.fit_predict(X)