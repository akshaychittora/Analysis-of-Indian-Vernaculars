# DM 
# Q4

import pandas as pd
import numpy as np
import json

df_census = pd.read_excel('DDW_PCA0000_2011_Indiastatedist.xlsx')
df_c18  = pd.read_excel('DDW-C18-0000.xlsx')
df_census_new= df_census[['Level','Name','TRU','TOT_P']].copy()
df_census_new['Name']=df_census_new['Name'].str.strip()
df_census_new= df_census_new[(df_census_new['Level']=="STATE")&(df_census_new['TRU']=="Total")]
df_c18 = df_c18.iloc[5:,:]
df_c18.rename( columns={'C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX':'State Code','Unnamed: 2':'Area','Unnamed: 3':'total','Unnamed: 4':'Age','Unnamed: 5':'2nd','Unnamed: 8':'3rd'}, inplace=True )
df_c18.head()

df_c18_new= df_c18[['State Code','Area','total','Age','2nd','3rd']].copy()
df_c18_new=df_c18_new[(df_c18_new['total']=='Total')&(df_c18_new['Age']=='Total')&(df_c18_new['Area']!='INDIA')]

one= []
for i, val in df_c18_new.iterrows():
    for j, val2 in df_census_new.iterrows():
        
        if(val['Area']==val2['Name']):
            one.append(int(val2['TOT_P'])-int(val['2nd']))
list1= df_c18_new['Area'].tolist()
list2= one
list3= df_c18_new['2nd'].tolist()
list4= df_c18_new['3rd'].tolist()
ratio=[]
for i in range(len(list1)):
    ratio.append([list1[i],list2[i],list3[i],list4[i]])

# ratio for 2 and 3
for i in range(len(ratio)):
    ratio[i][1]= float(ratio[i][2]/ratio[i][1])
    ratio[i][3]= float(ratio[i][3]/ratio[i][2])

ratio1= sorted(ratio,key=lambda x: x[3])
ans1=[]
x= len(ratio1)
ans1.extend([ratio1[x-1][0],ratio1[x-2][0],ratio1[x-3][0]])
ans1.extend([ratio1[0][0],ratio1[1][0],ratio1[2][0]])
# 3-to-2-ratio.csv
#x = {'state': ans1}
#df_ans2_1 = pd.DataFrame.from_dict(x)
#df_ans2_1.to_csv (r'3-to-2-ratio.csv', index = False, header=True) 



#2-to-1-ratio.csv
ratio1= sorted(ratio,key=lambda x: x[1])
ans2=[]
x= len(ratio1)
ans2.extend([ratio1[x-1][0],ratio1[x-2][0],ratio1[x-3][0]])
ans2.extend([ratio1[0][0],ratio1[1][0],ratio1[2][0]])
y = {'state': ans2}
df_ans2_2 = pd.DataFrame.from_dict(y)
df_ans2_2.to_csv (r'2-to-1-ratio.csv', index = False, header=True) 

