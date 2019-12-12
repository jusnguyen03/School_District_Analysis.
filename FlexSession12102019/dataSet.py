#%%
import pandas as pd
#%%
import os
#%%
#dataFile = os.path.join(os.getcwd(), 'FlexSession12102019\dataSet.csv')
dataFile = 'c:\\Users\\tan\\School_District_Analysis\\FlexSession12102019\\dataSet.csv'
#%%
dataFilePD = pd.read_csv(dataFile)

#%%
dateFilePD.head(100)

# %% 
dataFilePD.describe()
# %%
dataFilePD["Amount"],head(100)

# %%
dataFilePD["Amount"],describe()

# %%
dataFilePD[["Amount","Gender"]].head()

# %%
dataFilePD["Amount"].mean()

# %%
dataFilePD["Amount"].sum()

# %%
dataFilePD["Gender"].unique()

# %%
datafilePD["Gender"].value_counts()