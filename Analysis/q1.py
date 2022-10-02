# Assignment 2 DM

#Q1 

import json
import pandas as pd
import numpy as np
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
list1= df_c18_new['State Code'].tolist()
list2= one
list3= df_c18_new['2nd'].tolist()
list4= df_c18_new['3rd'].tolist()

x = {'state-code': list1,'percent-one':list2,'percent-two':list3,'percent-three':list4}
df_ans1 = pd.DataFrame.from_dict(x)
df_ans1.to_csv (r'percent-india.csv', index = False, header=True) 