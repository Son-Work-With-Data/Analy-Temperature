import pandas as pd
import os
import matplotlib.pyplot as plt

path = "C:\Data Analyst\Data\Data.xls" # changing the address please.
df = pd.read_excel(path)

#Changing the value of ** yeartt ** please
#Note : The value is from 1979 to 2020

yeartt = 2003 #######   <==============   CHANGING HERE 





##########################################################################################################

#Creat new columns and add the values into each new columns

df ['Month'] = pd.DatetimeIndex(df ['Date']).month

df ['Day'] = pd.DatetimeIndex(df ['Date']).day

df ['Year'] = pd.DatetimeIndex(df ['Date']).year

#Moving the column

df.insert(1,'Day',df.pop('Day'))

df.insert(2,'Month',df.pop('Month'))

df.insert(3,'Year',df.pop('Year'))

df['Date'] = pd.to_datetime(df['Date'])

#lHighest Temperature

HTemp = df[ ( df["Year"]== yeartt)  ]. groupby('Month') .max() ['max_temp']

print(HTemp)
 
Day =range (1,13)
col_map = plt.get_cmap('Paired')

plt.figure(figsize=[9, 6.5])
plt.bar(x= Day , height= HTemp,color=col_map.colors, edgecolor='k')
plt.xticks(Day, rotation=0)
plt.yticks(range (0,41), rotation=0)
plt.xlabel(' Months in ' + str(yeartt),size = 14)
plt.ylabel('The highest temperature on each Month',size = 14)
plt.show()

#lowest Temperature

LTemp = df[ ( df["Year"]== yeartt) & ( df["Month"]>0 )  ]. groupby('Month') .min() ['min_temp']

print(LTemp)

Day =range (1,13)
col_map = plt.get_cmap('Paired')

plt.figure(figsize=[7, 4])
plt.bar(x= Day , height= LTemp,color=col_map.colors, edgecolor='k')
plt.xticks(Day, rotation=0)
plt.yticks(range (-6,16), rotation=0)
plt.xlabel(' Months in ' + str(yeartt),size = 12)
plt.ylabel('The Lowest temperature on each Month',size = 10.5)
plt.show()