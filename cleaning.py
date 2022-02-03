import pandas as pd

df = pd.read_csv("Stars-Merged.csv")
df = df.drop(["Unnamed: 0"], axis = 1)
df = df.drop(["Unnamed: 6"], axis = 1)
df = df.drop(["Luminosity"], axis = 1)
df = df.drop(["star_name"], axis = 1)
df = df.drop(["distance"], axis = 1)
df = df.drop(["mass"], axis = 1)
df = df.drop(["radius"], axis = 1)

df.to_csv("Stars-Cleaned.csv")