#DM Q3

import json
import pandas as pd
import numpy as np
from scipy import stats
df_census = pd.read_excel('DDW_PCA0000_2011_Indiastatedist.xlsx')
df_c18  = pd.read_excel('DDW-C18-0000.xlsx')
df_census_new= df_census[['Level','Name','TRU','TOT_P']].copy()

df_census_new['Name']=df_census_new['Name'].str.strip()
df_census_new1= df_census_new[((df_census_new['Level']=="STATE")|(df_census_new['Level']=='India'))&(df_census_new['TRU']=="Rural")]
df_census_new2= df_census_new[((df_census_new['Level']=="STATE")|(df_census_new['Level']=='India'))&(df_census_new['TRU']=="Urban")]

df_c18 = df_c18.iloc[5:,:]
df_c18.rename( columns={'C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX':'State Code','Unnamed: 2':'Area','Unnamed: 3':'total','Unnamed: 4':'Age','Unnamed: 5':'2nd','Unnamed: 8':'3rd'}, inplace=True )
df_c18_new= df_c18[['State Code','Area','total','Age','2nd','3rd']].copy()
df_c18_new1=df_c18_new[(df_c18_new['total']=='Rural')&(df_c18_new['Age']=='Total')]
df_c18_new2=df_c18_new[(df_c18_new['total']=='Urban')&(df_c18_new['Age']=='Total')]

oneu= []
oner=[]
for i,val in df_c18_new1.iterrows():
    for j, val2 in df_census_new1.iterrows(): 
        if(val['Area'].lower()==val2['Name'].lower()):
            oner.append(int(val2['TOT_P'])-int(val['2nd']))
            
for i,val in df_c18_new2.iterrows():
    for j, val2 in df_census_new2.iterrows(): 
        if(val['Area'].lower()==val2['Name'].lower()):
            oneu.append(int(val2['TOT_P'])-int(val['2nd']))

twou=df_c18_new2['2nd'].tolist()

twor=df_c18_new1['2nd'].tolist()

threeu=df_c18_new2['3rd'].tolist()
threer=df_c18_new1['3rd'].tolist()
m= df_census_new2['TOT_P'].tolist()
f= df_census_new1['TOT_P'].tolist()

p=[]
for i in range(len(oneu)):
    p.append([oneu[i]/oner[i],twou[i]/twor[i],threeu[i]/threer[i]])

me=[]
for i in range(len(oneu)):
    x= m[i]/f[i]
    me.append([x,x,x])

p_value=[]
for i in range(len(me)):
    x,y=stats.ttest_ind(a=p[i],b=me[i],equal_var=False)
    p_value.append(y)



# part 1
list1= df_c18_new1['State Code'].tolist()
list2=[]
list3=[]
k=0
for i, val in df_census_new2.iterrows():
    list2.append(float(oneu[k]/val['TOT_P'])*100)
    k+=1
k=0
for i, val in df_census_new1.iterrows():
    list3.append(float(oner[k]/val['TOT_P'])*100)
    k+=1
list4=p_value

x = {'state-code': list1,' urban-percentage':list2,'rural-percentage':list3,' p-value':list4}
df_ans3 = pd.DataFrame.from_dict(x)
df_ans3.to_csv (r'geography-india-a.csv', index = False, header=True)


# part 2
list1= df_c18_new1['State Code'].tolist()
list2=[]
list3=[]
k=0
for i, val in df_census_new2.iterrows():
    list2.append(float(twou[k]/val['TOT_P'])*100)
    k+=1
k=0
for i, val in df_census_new1.iterrows():
    list3.append(float(twor[k]/val['TOT_P'])*100)
    k+=1
list4=p_value

y = {'state-code': list1,' urban-percentage':list2,'rural-percentage':list3,' p-value':list4}
df_ans3_2 = pd.DataFrame.from_dict(y)
df_ans3_2.to_csv (r'geography-india-b.csv', index = False, header=True)

# part 3
list1= df_c18_new1['State Code'].tolist()
list2=[]
list3=[]
k=0
for i, val in df_census_new2.iterrows():
    list2.append(float(threeu[k]/val['TOT_P'])*100)
    k+=1
k=0
for i, val in df_census_new1.iterrows():
    list3.append(float(threer[k]/val['TOT_P'])*100)
    k+=1
list4=p_value

z = {'state-code': list1,' urban-percentage':list2,'rural-percentage':list3,' p-value':list4}
df_ans3_3 = pd.DataFrame.from_dict(z)
df_ans3_3.to_csv (r'geography-india-c.csv', index = False, header=True)




