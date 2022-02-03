import pandas as pd
import plotly.express as px

df = pd.read_csv("Stars-Filtered.csv")

name = df["Star_name"].tolist()
distance = df["Distance"].tolist()
mass = df["Mass"].tolist()
radius = df["Radius"].tolist()
gravity = df["Gravity"].tolist()

#Star Name vs Distance
g1 = px.bar(
    df, 
    name, 
    distance, 
    color = name,
    title = "Star Name vs Distance Graph", 
    labels = {'x':'Name of Star', 'y':'Distance in Light Years'})
g1.update_layout(showlegend = False)
g1.show()

#Star Name vs Mass
g2 = px.bar(
    df, 
    name, 
    mass, 
    color = name,
    title = "Star Name vs Mass Graph", 
    labels = {'x':'Name of Star', 'y':'Mass in Earths'})
g2.update_layout(showlegend = False)
g2.show()

#Star Name vs Radius
g3 = px.bar(
    df, 
    name, 
    radius, 
    color = name,
    title = "Star Name vs Radius Graph", 
    labels = {'x':'Name of Star', 'y':'Radius in Earths'})
g3.update_layout(showlegend = False)
g3.show()

#Star Name vs Gravity
g4 = px.bar(
    df, 
    name, 
    gravity, 
    color = name,
    title = "Star Name vs Gravity Graph", 
    labels = {'x':'Name of Star', 'y':'Gravity'})
g4.update_layout(showlegend = False)
g4.show()