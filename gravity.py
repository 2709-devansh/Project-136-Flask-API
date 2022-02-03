import pandas as pd

df = pd.read_csv("Stars-Cleaned-Final.csv")
distance = df['Distance']
mass = df["Mass"]
radius = df["Radius"]
G = 6.67*(10**-11)

for i in range(0, len(distance)):
    distance[i] = distance[i].replace(",", "")   

df["Mass"] = df["Mass"]*1.989e+30
df["Radius"] = df["Radius"]*6.957e+8

gravity = []
for j in range(0, len(mass)):
    g = (G*mass[j])/(radius[j]**2)
    gravity.append(g)

df["Gravity"] = gravity

df.pop('Unnamed: 0')
df.to_csv("Stars-Gravity.csv")