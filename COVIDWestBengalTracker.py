

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

url = "https://www.mygov.in/covid-19/"

response = requests.get(url)
html = response.content


soup = BeautifulSoup(html, "html.parser")
soup.prettify


table = soup.find(name= 'table', attrs= {'id': 'state-covid-data'})
#print(table)
rows = table.find_all(name='tr')

columns = []
for row in rows:
    cols = row.find_all(name= ['th','td'])
    for col in cols:
        columns.append(col.text)

no_of_cols = len(rows[0].find_all(name= 'th'))
no_of_rows = len(rows)


data_country_wise = []
for i in range(0, no_of_rows):
    data_country_wise.append( columns[i*no_of_cols : i*no_of_cols + no_of_cols] )
#print(data_country_wise)



dataFrameIndex = []
for eachcountry in data_country_wise:
    dataFrameIndex.append(eachcountry[0])
dataFrameIndex = dataFrameIndex[1:]

dataFrameIndex = np.array(dataFrameIndex)
#print(dataFrameIndex)




#data_country_wise[0][1:]
dataFrameIndexTitle = data_country_wise[0][0]
dataFrameColumns = data_country_wise[0][1:]

dataFrameColumns = np.array(dataFrameColumns)
#print(dataFrameColumns)




data = data_country_wise[1:]
#print(data)
i = 0
for eachcountry in data:
    data[i] = eachcountry[1:]
    i=i+1
dataFrameData = data

dataFrameData = np.array(dataFrameData)



df = pd.DataFrame(data = dataFrameData, index= dataFrameIndex, columns= dataFrameColumns)
df.index.name = dataFrameIndexTitle
df.head()



dataWestBengal = df.loc['West Bengal']
state = dataWestBengal.name
stateIndex = dataWestBengal.index
stateValues = dataWestBengal.values
print("State: ", state)
print("Index: ", stateIndex)
print("Values: ", stateValues)




