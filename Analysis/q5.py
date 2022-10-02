#DM Q5

import pandas as pd
import numpy as np
import json

df_census = pd.read_excel('DDW_PCA0000_2011_Indiastatedist.xlsx')
df_c18  = pd.read_excel('DDW-C18-0000.xlsx')
df_census_new= df_census[['Level','Name','TRU','TOT_P']].copy()
df_census_new['Name']=df_census_new['Name'].str.strip()
df_census_new= df_census_new[((df_census_new['Level']=="STATE")|(df_census_new['Level']=='India'))&(df_census_new['TRU']=="Total")]

df_c18 = df_c18.iloc[5:,:]
df_c18.rename( columns={'C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX':'State Code','Unnamed: 2':'Area','Unnamed: 3':'total','Unnamed: 4':'Age','Unnamed: 5':'2nd','Unnamed: 8':'3rd'}, inplace=True )

df_c18_new= df_c18[['State Code','Area','total','Age','3rd']].copy()
df_c18_new=df_c18_new[(df_c18_new['total']=='Total')&(df_c18_new['Age']!='Total')]

one= []
max1=0
ag=[]
for i, val in df_census_new.iterrows():
    max1=0
    one.append(0)
    ag.append('$')
    #print(one)
    for j, val2 in df_c18_new.iterrows(): 
        if(val2['Area'].lower()==val['Name'].lower()):
            x= float(int(val2['3rd'])/int(val['TOT_P']))*100
            if(one[-1]<x):
                one[-1]= x
                ag[-1]=val2['Age']
                
list1= df_census_new['Name'].tolist()
x = {'state/ut': list1,'age-group':ag,'percantage':one}
df_ans3 = pd.DataFrame.from_dict(x)
df_ans3.to_csv (r'age-india.csv', index = False, header=True)               
            

            

