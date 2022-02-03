import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Stars-Gravity.csv")
df.pop("Unnamed: 0")
#df = df.drop(72, axis = 0) this star has a gravity of 34240 much much bigger than the others

mass = df["Mass"]
radius = df["Radius"]
gravity = df["Gravity"]

fig1 = plt.figure(figsize = (15, 10))
plt.scatter(mass, radius, c = "blue", marker = "*", linewidths = 2, edgecolor = "blue")
plt.xlabel("Mass")
plt.ylabel("Radius")
plt.title("Graph for Masses and Radii")
plt.show()

fig2 = plt.figure(figsize = (15, 10))
plt.scatter(mass, gravity, c = "yellow", marker = "*", linewidths = 2, edgecolor = "red")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.title("Graph for Masses and Gravities")
plt.show()