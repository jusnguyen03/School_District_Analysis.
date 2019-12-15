#%%
import pandas as pd
#%%
csvFile: str = "LiveSession4_12122019/ufoSightings.csv"

#read this csv into a pandas dataframe
ufoDF = pd.read_csv(csvFile)
print(ufoDF.count())


# %%
#All rows are populated
cleanUFODF = ufoDF.dropna(how='any')
print(cleanUFODF.count())

# %%
cleanUFODF["duration (seconds)"].apply(type)

# %%
castDurationDF = cleanUFODF.copy()
castDurationDF["duration (seconds)"] = castDurationDF.loc[:, "duration (seconds)"].astype(float)
castDurationDF["duration (seconds)"].apply(type)
castDurationDF.count()

# %%
usaOnlySightings = castDurationDF.loc[castDurationDF["country"] == "us", :]
usaOnlySightings.count()
# %%
stateCounts = usaOnlySightings["state"].value_counts()


# %%
groupByState = usaOnlySightings.groupby(['state'])
print(groupByState)
groupByStateValues = groupByState.count()

# %%
groupByStateDurationSumDF = groupByState["duration (seconds)"].sum()
groupByStateDurationAVGDF = groupByState["duration (seconds)"].mean()

# %%
groupByCity = usaOnlySightings.groupby(['city'])
groupByCityAvgSeries = groupByCity["duration (seconds)"].mean()

# %%
groupByCityState = usaOnlySightings.groupby(['city','state'])
groupByCityStateAvg = groupByCityState["duration (seconds)"].mean()


# %%
groupByCityStateAvg.head(100)

# %%
groupByCityStateAvg.loc[groupByCityStateAvg["duration (seconds)"] > 17541380, :]

# %%
groupByCityStateAvg.max()


# %%
groupByCityStateAvg.idxmax()


# %%
