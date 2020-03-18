import pandas as pd

df = pd.read_csv("VTSAX.csv")
df = pd.concat([df["Date"].str.extract(r'(.*)-(.*)-(.*)'), df], axis = 1)
df = df.rename(columns={0: "Year", 1: "Month", 2:"Day"})

print(df)

df.to_csv("VTSAX_cleaned.csv", index=False)