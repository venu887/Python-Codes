#!/usr/bin/env python
# coding: utf-8

# In[9]:


##Import CSV files or datasets
# import library called Pandas
import pandas as pd
import numpy as np


# In[10]:


df2 =pd.read_excel (r"J:\\Venu personal\Venu_py_Linux\\CCLE annotations.xlsx")
#place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
print(df2)


# In[3]:


df2.tail()


# In[6]:


df2.head()


# In[ ]:


df2.groupby('release_year')['title'].count().plot(title='Films By Year')


# In[11]:


df2.index
df2.columns


# In[14]:


# Object creation by pandas and numpy
s= pd.Series([1,3,4,5,np.nan,6,7,9])
s


# In[24]:


dates = pd.date_range("20220801", periods=6)
dates


# In[33]:


dt = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list("ABCD"))
dt


# In[38]:


dt2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20220815"),
        "C": pd.Series(1, index=list(range(4)),dtype="float32"),
        "D": np.array([3]*4, dtype="int32"),
        "E": pd.Categorical(["test","train","test", "train"]),
        "F": "foo",
    }
)
dt2


# In[39]:


dt2.dtypes


# In[43]:


dt2.index


# In[44]:


dt2.columns


# In[45]:


dt2.to_numpy()


# In[48]:


dt.to_numpy()
dt2.to_numpy()


# In[49]:


dt.describe()


# In[50]:


df2.describe()


# In[53]:


dt.T


# In[55]:


# Sortining by an axis, column names
dt.sort_index(axis=1, ascending=False)


# In[57]:


# Sorting by value in colunm B
dt.sort_values(by="B")


# In[58]:


# Selection-the optimized pandas data access methods, .at, .iat, .loc and .iloc.
dt["A"] # only select column A 


# In[60]:


# only selecting the rows use Zero to row1,row2...
dt[0:2]


# In[62]:


# select only using row names with all column data
dt["20220801":"20220802"]


# In[64]:


# Selection by label first row starts at ZERO with all column
dt.loc[dates[0]]


# In[65]:


# Selecting multiaxis labels like selection for first columns with all rows
dt.loc[:, ["A","B"]]


# In[72]:


# selection of label slicing, both endpoints row*Column 
# Select any rows and any columns here
dt.loc["20220801":"20220804", ["A","C"]]


# In[71]:


# OR select one row with two columns
dt.loc["20220801",["A","B"]]


# In[73]:


# getting scalar value
dt.loc[dates[0], "A"]


# In[74]:


# another method for getting scalar value
dt.at[dates[0],"A"]


# In[75]:


# Selected by position forth row all columns
dt.iloc[3]


# In[78]:


# Selected by specific row and columns 
dt.iloc[2:4, 0:2]


# In[81]:


#Numpy
dt.iloc[[1,2,3],[0,1,2]]


# In[82]:


dt.iloc[1:3, : ] # slicing rows explicitly


# In[83]:


# slicing columns explicitly
dt.iloc[: , 1:3]


# In[84]:


dt.iloc[1,1]


# In[86]:


dt.iat[1,1]


# In[88]:


#Boolean indexing Using a single column’s values to select data
dt[dt["A"]>0.5]


# In[89]:


# Selecting values from a DataFrame where a boolean condition is met
dt[dt>0.2]


# In[92]:


dt3=dt.copy()


# In[95]:


# Adding new column to the existing column
dt3["E"] = ["one","two", "two", "three", "four", "five"]


# In[96]:


dt3


# In[97]:


dt3[dt3["E"].isin(["two", "three"])]


# In[114]:


# Setting a new column automatically aligns the data by the indexes
S2 = pd.Series([1,2,3,4,5,6], index=pd.date_range("20220802", periods=6))
S2


# In[106]:


# Replacing first position with Zero or Setting values by label
dt.at[dates[0], "A"]=0
dt


# In[109]:


#Setting values by position
dt.iat[0,2]=0


# In[110]:


dt


# In[111]:


#Setting by assigning with a NumPy array
dt.loc[:, "D"]=np.array([5]*len(dt))


# In[112]:


dt


# In[115]:


dt["F"]=S2


# In[116]:


dt


# In[118]:


dt2 = dt.copy()
dt2


# In[119]:


dt2[dt2>0]=-dt2


# In[120]:


dt2


# In[124]:


# Missing data (np.nan)
dt1=dt.reindex(index=dates[0:4], columns=list(dt.columns)+["E"])
dt1.loc[dates[0]:dates[1], "E"]=1
dt1


# In[125]:


# To drop any rows that have missing data
dt1.dropna(how="any")


# In[126]:


# Filling missing data
dt1.fillna(value=5)


# In[129]:


# To get the boolean mask where values are nan
pd.isna(dt1)


# In[130]:


# Operations
dt.mean() # Each column mean


# In[131]:


dt.mean(1) # Each row mean 


# In[132]:


# data joining and merging 
left=pd.DataFrame({"key":["foo", "foo"], "lval":[1,2]})
right=pd.DataFrame({"key":["foo", "foo"],"rval":[4,5]})


# In[133]:


left


# In[134]:


right


# In[135]:


pd.merge(left,right, on="key")


# In[139]:


# Grouping-Splitting, Applying, Combining
df3=pd.DataFrame(
{
    "A":["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
    "B":["one", "one", "two", "three", "two", "two", "one", "three"],
    "C":np.random.randn(8),
    "D":np.random.randn(8)
}
)
df3


# In[141]:


#Grouping and then applying the sum() function to the resulting
df3.groupby("A").sum()


# In[143]:


# Grouping by multiple columns 
df3.groupby(["A", "B"]).sum()


# In[144]:


# Reshaping-Stack
tuples=list(
zip(*[
    ["bar", "bar", "baz", "baz", "foo", "foo","qux", "qux"],
    ["one", "two", "one", "two", "one","two", "one", "two"],
])
)


# In[145]:


tuples


# In[146]:


index=pd.MultiIndex.from_tuples(tuples, names=["first", "second"])


# In[147]:


df=pd.DataFrame(np.random.randn(8,2), index=index,columns=["A", "B"])


# In[151]:


df4=df[:4]


# In[152]:


df4


# In[153]:


# The stack() method “compresses” a level in the DataFrame’s columns:
stacked=df4.stack()


# In[154]:


stacked 


# In[155]:


stacked.unstack()


# In[156]:


stacked.unstack(1)


# In[157]:


stacked.unstack(0)


# In[161]:


df=pd.DataFrame(
{
    "A":["one", "one", "two", "three"]*3,
    "B":["A", "B", "C"]*4,
    "C":["foo", "foo", "foo", "bar", "bar", "bar"]*2,
    "D": np.random.randn(12),
    "E": np.random.randn(12),
}
)


# In[162]:


df


# In[166]:


# pivot tables from this data very easily
# design data as you like by using single specific names
pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])


# In[168]:


df2.head()


# In[170]:


# Time series
rng=pd.date_range("1/1/2022", periods=100, freq="S")


# In[172]:


rng


# In[175]:


ts=pd.Series(np.random.randint(0,500,len(rng)), index=rng)


# In[177]:


ts.resample("5Min").sum()


# In[ ]:




