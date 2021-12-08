import pandas as pd
df= pd.read_csv("input_files/day02.txt", sep=" ", header=None)
df.columns = ["Direction","Magnitude"]
h = 0
v = 0
aim = 0
for i in df.index:
    m = df.loc[i,"Magnitude"]
    if df.loc[i,"Direction"] == "forward":
        h += m
    elif df.loc[i,"Direction"] == "down":
        v += m
    elif df.loc[i,"Direction"] == "up":
        v -= m

print(h,v,h*v)

h = 0
v = 0
aim = 0
for i in df.index:
    m = df.loc[i,"Magnitude"]
    if df.loc[i,"Direction"] == "forward":
        h += m
        v += aim * m
    elif df.loc[i,"Direction"] == "down":
        # v += m
        aim += m
    elif df.loc[i,"Direction"] == "up":
        # v -= m
        aim -= m

print(h,v,h*v)
