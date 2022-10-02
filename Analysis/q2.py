#DM Q2

import json
import pandas as pd
import numpy as np
from scipy import stats
df_census = pd.read_excel('DDW_PCA0000_2011_Indiastatedist.xlsx')
df_c18  = pd.read_excel('DDW-C18-0000.xlsx')
df_census_new= df_census[['Level','Name','TRU','TOT_P','TOT_M','TOT_F']].copy()

df_census_new['Name']=df_census_new['Name'].str.strip()
df_census_new= df_census_new[((df_census_new['Level']=="STATE")|(df_census_new['Level']=='India'))&(df_census_new['TRU']=="Total")]

df_c18 = df_c18.iloc[5:,:]
df_c18.rename( columns={'C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX':'State Code','Unnamed: 2':'Area','Unnamed: 3':'total','Unnamed: 4':'Age','Unnamed: 6':'m2nd','Unnamed: 7':'f2nd','Unnamed: 9':'m3rd','Unnamed: 10':'f3rd'}, inplace=True )
df_c18_new= df_c18[['State Code','Area','total','Age','m2nd','f2nd','m3rd','f3rd']].copy()
df_c18_new=df_c18_new[(df_c18_new['total']=='Total')&(df_c18_new['Age']=='Total')]
onem= []
onef=[]
for i, val in df_c18_new.iterrows():
    for j, val2 in df_census_new.iterrows():
        
        if(val['Area'].lower()==val2['Name'].lower()):
            onem.append(int(val2['TOT_M'])-int(val['m2nd']))
            onef.append(int(val2['TOT_F'])-int(val['f2nd']))

twom= df_c18_new['m2nd'].tolist()
twof=df_c18_new['f2nd'].tolist()
threem=df_c18_new['m3rd'].tolist()
threef=df_c18_new['f3rd'].tolist()
m= df_census_new['TOT_M'].tolist()
f= df_census_new['TOT_F'].tolist()
p=[]
for i in range(len(onem)):
    p.append([onem[i]/onef[i],twom[i]/twof[i],threem[i]/threef[i]])

me=[]
for i in range(len(onem)):
    x= m[i]/f[i]
    me.append([x,x,x])

p_value=[]
for i in range(len(me)):
    x,y=stats.ttest_ind(a=p[i],b=me[i],equal_var=False)
    p_value.append(y)


# part 1
list1= df_c18_new['State Code'].tolist()
list2=[]
list3=[]
k=0
for i, val in df_census_new.iterrows():
    list2.append(float(onem[k]/val['TOT_M'])*100)
    list3.append(float(onef[k]/val['TOT_F'])*100)
    k+=1
list4=p_value

x = {'state-code': list1,' male-percentage':list2,'female-percentage':list3,' p-value':list4}
df_ans2 = pd.DataFrame.from_dict(x)
df_ans2.to_csv (r'gender-india-a.csv', index = False, header=True)


# part 2
list1= df_c18_new['State Code'].tolist()
list2=[]
list3=[]
k=0
for i, val in df_census_new.iterrows():
    list2.append(float(twom[k]/val['TOT_M'])*100)
    list3.append(float(twof[k]/val['TOT_F'])*100)
    k+=1
list4=p_value

y = {'state-code': list1,' male-percentage':list2,'female-percentage':list3,' p-value':list4}
df_ans2_2 = pd.DataFrame.from_dict(y)
df_ans2_2.to_csv (r'gender-india-b.csv', index = False, header=True)

# part 3
list1= df_c18_new['State Code'].tolist()
list2=[]
list3=[]
k=0
for i, val in df_census_new.iterrows():
    list2.append(float(threem[k]/val['TOT_M'])*100)
    list3.append(float(threef[k]/val['TOT_F'])*100)
    k+=1
list4=p_value

z = {'state-code': list1,' male-percentage':list2,'female-percentage':list3,' p-value':list4}
df_ans2_3 = pd.DataFrame.from_dict(x)
df_ans2_3.to_csv (r'gender-india-c.csv', index = False, header=True)

