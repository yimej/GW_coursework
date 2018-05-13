

```python
import json
import pandas as pd
import numpy as np
```


```python
with open("purchase_data.json") as datafile:
    data = json.load(datafile)
df = pd.DataFrame(data)
df = df[["SN", "Age", "Gender", "Item ID", "Price", "Item Name"]]
df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SN</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Price</th>
      <th>Item Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Aelalis34</td>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>3.37</td>
      <td>Bone Crushing Silver Skewer</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Eolo46</td>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>2.32</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Assastnya25</td>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>2.46</td>
      <td>Primitive Blade</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Pheusrical25</td>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>1.36</td>
      <td>Final Critic</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Aela59</td>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>1.27</td>
      <td>Stormfury Mace</td>
    </tr>
  </tbody>
</table>
</div>




```python
#PLAYER COUNT
total = df["SN"].nunique()
totalPlayers = pd.DataFrame([{"Total Players":str(total)}])
totalPlayers
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Purchasing Analysis (Total)
numItems = df["Item ID"].nunique()

avePrice = round(df["Price"].mean(), 2)
totalPurchases = df["Price"].count()
totalRevenue = round(df["Price"].sum(), 2)
totalPur_df = pd.DataFrame({"Number of Unique Items":[str(numItems)],
                            "Average Price":["$"+str(avePrice)],
                            "Number of Purchases":[str(totalPurchases)],
                            "Total Revenue":["$"+str(totalRevenue)]},
                           columns=["Number of Unique Items", "Average Price", "Number of Purchases",
                                    "Total Revenue"])
totalPur_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>183</td>
      <td>$2.93</td>
      <td>780</td>
      <td>$2286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Gender Demographics
totalPlayers = pd.DataFrame([{"Total Players":str(df["SN"].nunique())}])

male_df = df.loc[df["Gender"] == "Male"]
male = male_df["SN"].nunique()
malePer = round((100 * male / total), 2)

female_df = df.loc[df["Gender"] == "Female"]
female = female_df["SN"].nunique()
femalePer = round((100 * female / total), 2)

other_df = df.loc[df["Gender"] == "Other / Non-Disclosed"]
other = other_df["SN"].nunique()
otherPer = round((100 * other / total), 2)

gender_df = pd.DataFrame({"Total Count":[str(male), str(female), str(other)],
                          "Percentage of Players":[(str(malePer)+"%"), 
                                                   (str(femalePer)+"%"), 
                                                   (str(otherPer)+"%")]},
                        index = ["Male", "Female", "Other/Non-Disclosed"])
gender_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.15%</td>
      <td>465</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.45%</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Other/Non-Disclosed</th>
      <td>1.4%</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Purchasing Analysis (Gender)
male_count = len(male_df)
male_avePrice = round(male_df["Price"].mean(), 2)
male_totalPurchases = round(male_df["Price"].sum(), 2)
male_normTotal = round(male_df["Price"].sum() / male, 2)

female_count = len(female_df)
female_avePrice = round(female_df["Price"].mean(), 2)
female_totalPurchases = round(female_df["Price"].sum(), 2)
female_normTotal = round(female_df["Price"].sum() / female, 2)

other_count = len(other_df)
other_avePrice = round(other_df["Price"].mean(), 2)
other_totalPurchases = round(other_df["Price"].sum(), 2)
other_normTotal = round(other_df["Price"].sum() / other, 2)

totalPurGender = pd.DataFrame({"Purchase Count":[male_count, female_count, other_count],
                               "Average Purchase Price":[("$"+str(male_avePrice)),
                                                         ("$"+str(female_avePrice)),
                                                         ("$"+str(other_avePrice))],
                               "Total Purchase Value":[("$"+str(male_totalPurchases)),
                                                       ("$"+str(female_totalPurchases)),
                                                       ("$"+str(other_totalPurchases))],
                               "Normalized Totals":[("$"+str(male_normTotal)),
                                                    ("$"+str(female_normTotal)),
                                                    ("$"+str(other_normTotal))]},
                              index = ["Male", "Female", "Other/Non-Disclosed"],
                              columns = ["Purchase Count", "Average Purchase Price",
                                        "Total Purchase Value", "Normalized Totals"])
totalPurGender
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>$2.95</td>
      <td>$1867.68</td>
      <td>$4.02</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>$2.82</td>
      <td>$382.91</td>
      <td>$3.83</td>
    </tr>
    <tr>
      <th>Other/Non-Disclosed</th>
      <td>11</td>
      <td>$3.25</td>
      <td>$35.74</td>
      <td>$4.47</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Age Demographics
bins = [0, 9, 14, 19, 24, 29, 34, 39, (df["Age"].max() + 1)]
ageGroupRows = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40<"]
ageData = []

df["Age Group"] = pd.cut(df["Age"], bins, labels = ageGroupRows)

unique_df = df.drop_duplicates("SN")
ageGroup = pd.cut(unique_df["Age"], bins, labels = ageGroupRows)
ageGroup_df = pd.DataFrame(ageGroup)
ageGroup_df = pd.DataFrame(ageGroup_df["Age"].value_counts(), index = ageGroupRows)
ageGroup_df = ageGroup_df.rename(columns = {"Age":"Total Count"})

percentByAge = round(ageGroup_df["Total Count"] / total * 100, 2)
ageGroup_df["Percentage of Players"] = percentByAge

ageGroup_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Count</th>
      <th>Percentage of Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>19</td>
      <td>3.32</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>23</td>
      <td>4.01</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>100</td>
      <td>17.45</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>259</td>
      <td>45.20</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>87</td>
      <td>15.18</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>47</td>
      <td>8.20</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>27</td>
      <td>4.71</td>
    </tr>
    <tr>
      <th>40&lt;</th>
      <td>11</td>
      <td>1.92</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Purchasing Analysis (Age)
ageData=[]
ageColumns = ["Purchase Count", "Average Purchase Price", "Total Purchase Value", "Normalized Totals"]

for i in ageGroupRows:
    loop_df = df.loc[df["Age Group"] == i]
    loop_numPlayers = len(unique_df.loc[df["Age Group"] == i])
    loop_count = len(loop_df)
    loop_avePrice = round(loop_df["Price"].mean(), 2)
    loop_totalPurchases = round(loop_df["Price"].sum(), 2)
    loop_normTotal = round(loop_df["Price"].sum() / loop_numPlayers, 2)
    ageData.append([loop_count, ("$"+str(loop_avePrice)), ("$"+str(loop_totalPurchases)), 
                ("$"+str(loop_normTotal))])
    
age_df = pd.DataFrame(ageData, columns = ageColumns, index = ageGroupRows)
age_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>28</td>
      <td>$2.98</td>
      <td>$83.46</td>
      <td>$4.39</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>35</td>
      <td>$2.77</td>
      <td>$96.95</td>
      <td>$4.22</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>133</td>
      <td>$2.91</td>
      <td>$386.42</td>
      <td>$3.86</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>336</td>
      <td>$2.91</td>
      <td>$978.77</td>
      <td>$3.78</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>125</td>
      <td>$2.96</td>
      <td>$370.33</td>
      <td>$4.26</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>64</td>
      <td>$3.08</td>
      <td>$197.25</td>
      <td>$4.2</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>42</td>
      <td>$2.84</td>
      <td>$119.4</td>
      <td>$4.42</td>
    </tr>
    <tr>
      <th>40&lt;</th>
      <td>17</td>
      <td>$3.16</td>
      <td>$53.75</td>
      <td>$4.89</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Top Spenders
findNames_df = pd.DataFrame((df.reset_index().groupby("SN").sum()))
findNames_df = findNames_df.sort_values("Price", ascending=False)
findNames_df = findNames_df.head(5)
findNames_df = findNames_df.reset_index()
findNames_df = findNames_df[["SN","Price"]]

topSpendersNames = findNames_df["SN"].tolist()
spendersColumns = ["SN", "Purchase Count", "Average Purchase Price", "Total Purchase Value"]
topSpenders = []

for i in topSpendersNames:
    topPlayer_df = df.loc[df["SN"] == i]
    topPlayer_count = len(topPlayer_df)
    topPlayer_average = round(topPlayer_df["Price"].mean(), 2)
    topPlayer_sum = round(topPlayer_df["Price"].sum(), 2)
    topSpenders.append([i, topPlayer_count, ("$"+str(topPlayer_average)), ("$"+str(topPlayer_sum))])
    
spenders_df = pd.DataFrame(topSpenders, columns = spendersColumns)
spenders_df.set_index("SN")
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>5</td>
      <td>$3.41</td>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4</td>
      <td>$3.39</td>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4</td>
      <td>$3.18</td>
      <td>$12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>3</td>
      <td>$4.24</td>
      <td>$12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3</td>
      <td>$3.86</td>
      <td>$11.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Most Popular Items
findPopular_df = df
findPopular_df["Count"] = ""
findPopular_df = pd.DataFrame((findPopular_df.reset_index().groupby(["Item Name", "Item ID"]).count()))
findPopular_df = findPopular_df.sort_values("Price", ascending=False)
findPopular_df = findPopular_df.head(5)
findPopular_df = findPopular_df.reset_index()
findPopular_df = findPopular_df[["Item Name", "Item ID", "Count"]]

popularItemNames = findPopular_df["Item Name"].tolist()
popularItemIDs = findPopular_df["Item ID"].tolist()
popularColumns = ["Item Name", "Purchase Count", "Item Price", "Total Purchase Value"]
popular = []

for i in popularItemNames:
    popular_df = df.loc[df["Item Name"] == i]
    popular_count = len(popular_df)
    popular_price = round(popular_df["Price"].mean(), 2)
    popular_sum = round(popular_df["Price"].sum(), 2)
    popular.append([i, popular_count, ("$"+str(popular_price)), ("$"+str(popular_sum))])#popularItemIDs, popularItemNames, 

popular_df = pd.DataFrame(popular, columns = popularColumns)
popular_df["Item ID"] = popularItemIDs
popular_df = popular_df.set_index(["Item ID", "Item Name"])
popular_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>$2.35</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>11</td>
      <td>$2.23</td>
      <td>$24.53</td>
    </tr>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>9</td>
      <td>$2.07</td>
      <td>$18.63</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>9</td>
      <td>$1.49</td>
      <td>$13.41</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Most Profitable Items
findProfitable_df = df
findProfitable_df = pd.DataFrame((findProfitable_df.reset_index().groupby(["Item Name", "Item ID"]).sum()))
findProfitable_df = findProfitable_df.sort_values("Price", ascending=False)
findProfitable_df = findProfitable_df.head(5)
findProfitable_df = findProfitable_df.reset_index()
findProfitable_df = findProfitable_df[["Item Name", "Item ID", "Price"]]

profitableItemNames = findProfitable_df["Item Name"].tolist()
profitableItemIDs = findProfitable_df["Item ID"].tolist()
profitableColumns = ["Item Name", "Purchase Count", "Item Price", "Total Purchase Value"]
profitable = []

for i in profitableItemNames:
    profit_df = df.loc[df["Item Name"] == i]
    profit_count = len(profit_df)
    profit_price = round(profit_df["Price"].mean(), 2)
    profit_sum = round(profit_df["Price"].sum(), 2)
    profitable.append([i, profit_count, ("$"+str(profit_price)), ("$"+str(profit_sum))])

profit_df = pd.DataFrame(profitable, columns = profitableColumns)
profit_df["Item ID"] = profitableItemIDs
profit_df = profit_df.set_index(["Item ID", "Item Name"])
profit_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>7</td>
      <td>$4.25</td>
      <td>$29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>6</td>
      <td>$4.95</td>
      <td>$29.7</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>6</td>
      <td>$4.87</td>
      <td>$29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>8</td>
      <td>$3.61</td>
      <td>$28.88</td>
    </tr>
  </tbody>
</table>
</div>


