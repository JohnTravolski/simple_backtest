import pandas as pd

df_all_years = pd.read_csv("VTSAX_cleaned.csv")

years = list(range(2001, 2020))
num_places = {xx:[0,0,0,0] for xx in ["Lump", "Monthly", "Biweekly", "Weekly"]} # number of years each method ranked in each position (1st through 4th)

for year in years:
  df = df_all_years.loc[df_all_years["Year"] == year]

  thismonth = 0
  monthly_rows = []
  for index, row in df.iterrows():
    if row["Month"] != thismonth:
      thismonth += 1
      monthly_rows.append(row)

  df_weekly = df.iloc[::5, :]
  df_biweekly = df.iloc[::10, :]
  df_monthly = pd.DataFrame(monthly_rows)

  # lump sum calc
  lump = 6000
  num_shares = lump/df.iloc[0]["Close"] # num shares at beginning of year
  lump_endval = num_shares*df.iloc[-1]["Close"]

  # monthly calc
  init = 0
  contrib = lump/df_monthly.shape[0]
  num_shares = init/df.iloc[0]["Close"] # num shares at beginning of year
  for index, row in df_monthly.iterrows():
    num_shares += contrib/row["Close"]
  monthly_endval = num_shares*df.iloc[-1]["Close"]

  # biweekly calc
  init = 0
  contrib = lump/df_biweekly.shape[0]
  num_shares = init/df.iloc[0]["Close"] # num shares at beginning of year
  for index, row in df_biweekly.iterrows():
    num_shares += contrib/row["Close"]
  biweekly_endval = num_shares*df.iloc[-1]["Close"]

  # weekly calc
  init = 0
  contrib = lump/df_weekly.shape[0]
  num_shares = init/df.iloc[0]["Close"] # num shares at beginning of year
  for index, row in df_weekly.iterrows():
    num_shares += contrib/row["Close"]
  weekly_endval = num_shares*df.iloc[-1]["Close"]
  
  winners = sorted([("Lump", lump_endval), ("Monthly", monthly_endval), ("Biweekly", biweekly_endval), ("Weekly", weekly_endval)], key = lambda x: x[1], reverse=True)
  
  for pos, tup in enumerate(winners):
    name, val = tup
    num_places[name][pos] += 1
  
  print(year, winners)

print(num_places)