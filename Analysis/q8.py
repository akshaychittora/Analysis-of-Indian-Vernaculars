# DM Q8

import pandas as pd
import numpy as np
import json

df_census = pd.read_excel('DDW_PCA0000_2011_Indiastatedist.xlsx')
df_c14= pd.read_excel('DDW-0000C-14.xls')
df_c18 = pd.read_excel('DDW-C18-0000.xlsx')
df_census_new= df_census[['Level','Name','TRU','TOT_P']].copy()
df_census_new['Name']=df_census_new['Name'].str.strip()
df_census_new= df_census_new[((df_census_new['Level']=="STATE")|(df_census_new['Level']=='India'))&(df_census_new['TRU']=="Total")]

df_c14= pd.read_excel('DDW-0000C-14.xls')
df_c14 = df_c14.iloc[6:,:]
df_c14.rename(columns={'C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ':'age','Unnamed: 3': 'state','Unnamed: 6':'tm','Unnamed: 7':'tf'}, inplace=True )
df_c14_new= df_c14[['state','age','tm','tf']].copy()

temp= 'INDIA'
flag1=0
flag2=0
for i, val in df_c14_new.iterrows():
    if(val['state']==temp):
        if(val['age']=='30-34'):
            flag1=1
            x=0
            y=0
        if(flag1==1 and val['age']!='45-49'):
            x= x+ val['tm']
            y=y+ val['tf']
        if(val['age']=='45-49'):
            val['age']='30-49'
            val['tm']= x
            val['tf']=y
            flag1=0
        
        if(val['age']=='50-54'):
            flag2=1
            x=0
            y=0
        if(flag2==1 and val['age']!='65-69'):
            x= x+ val['tm']
            y=y+ val['tf']
        if(val['age']=='65-69'):
            val['age']='50-69'
            val['tm']=x
            val['tm']=y
            flag2=0
    else:
        temp=val['state']
        
for i, val in df_c14_new.iterrows():
    if(val['state']!='India'):
    
        val['state']= val['state'][8: -5]
    if(val['age']=='70-74'):
        val['age']='70+'

df_c18 = df_c18.iloc[5:,:]
df_c18.rename( columns={'C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX':'State Code','Unnamed: 2':'Area','Unnamed: 3':'total','Unnamed: 4':'Age','Unnamed: 6':'m2nd','Unnamed: 7':'f2nd','Unnamed: 9':'m3rd','Unnamed: 10':'f3rd'}, inplace=True )

df_c18_new= df_c18[['State Code','Area','total','Age','m2nd','f2nd','m3rd','f3rd']].copy()
df_c18_new=df_c18_new[(df_c18_new['total']=='Total')&(df_c18_new['Age']!='Total')]

# for three or more languages.
one1= []
one2=[]
max1=0
ag1=[]
ag2=[]

tm=[]
tf=[]
for i,val in df_c18_new.iterrows():
    for j,val2 in df_c14_new.iterrows():
            if(val['Area'].lower()== val2['state'].lower() and val['Age']==val2['age']):
                tm.append(val2['tm'])
                tf.append(val2['tf'])
        
index=0
for i, val in df_census_new.iterrows():
    max1=0
    one1.append(0)
    ag1.append('$')
    one2.append(0)
    ag2.append('$')
    #print(one)
    index=0
    for j, val2 in df_c18_new.iterrows(): 
        if(val2['Area'].lower()==val['Name'].lower()):
            x= float(int(val2['m3rd'])/tm[index])
            index+=1
            if(one1[-1]<x):
                one1[-1]= x
                ag1[-1]=val2['Age']
    index=0
    for j, val2 in df_c18_new.iterrows(): 
        if(val2['Area'].lower()==val['Name'].lower()):
            x= float(int(val2['f3rd'])/tf[index])
            index+=1
            if(one2[-1]<x):
                one2[-1]= x
                ag2[-1]=val2['Age']
                
list1= df_census_new['Name'].tolist()
x = {'state/ut': list1,'age-group-males':ag1,'ratio-males':one1,'age-group-females':ag2,'ratio-females': one2}
df_ans8 = pd.DataFrame.from_dict(x)
df_ans8.to_csv (r'age-gender-a.csv', index = False, header=True) 

# for two languages.
one1= []
one2=[]
max1=0
ag1=[]
ag2=[]
for i, val in df_census_new.iterrows():
    max1=0
    index=0
    one1.append(0)
    ag1.append('$')
    one2.append(0)
    ag2.append('$')
    #print(one)
    for j, val2 in df_c18_new.iterrows(): 
        if(val2['Area'].lower()==val['Name'].lower()):
            x= float(int(val2['m2nd'])/tm[index])
            index+=1
            if(one1[-1]<x):
                one1[-1]= x
                ag1[-1]=val2['Age']
    index=0
    for j, val2 in df_c18_new.iterrows(): 
        if(val2['Area'].lower()==val['Name'].lower()):
            x= float(int(val2['f2nd'])/tf[index])
            index+=1
            if(one2[-1]<x):
                one2[-1]= x
                ag2[-1]=val2['Age']
                
list1= df_census_new['Name'].tolist()
x = {'state/ut': list1,'age-group-males':ag1,'ratio-males':one1,'age-group-females':ag2,'ratio-females': one2}
df_ans8 = pd.DataFrame.from_dict(x)
df_ans8.to_csv (r'age-gender-b.csv', index = False, header=True) 



# for one language

one1= []
one2=[]
max1=0
ag1=[]
ag2=[]
for i, val in df_census_new.iterrows():
    max1=0
    one1.append(0)
    ag1.append('$')
    one2.append(0)
    ag2.append('$')
    index=0
    #print(one)
    for j, val2 in df_c18_new.iterrows(): 
        if(val2['Area'].lower()==val['Name'].lower()):
            x= float((tm[index]-int(val2['m2nd']))/tm[index])
            index+=1
            if(one1[-1]<x):
                one1[-1]= x
                ag1[-1]=val2['Age']
    index=0
    for j, val2 in df_c18_new.iterrows(): 
        if(val2['Area'].lower()==val['Name'].lower()):
            x= float((tf[index]-int(val2['m2nd']))/tf[index])
            index+=1
            if(one2[-1]<x):
                one2[-1]= x
                ag2[-1]=val2['Age']
                
list1= df_census_new['Name'].tolist()
x = {'state/ut': list1,'age-group-males':ag1,'ratio-males':one1,'age-group-females':ag2,'ratio-females': one2}
df_ans8 = pd.DataFrame.from_dict(x)
df_ans8.to_csv (r'age-gender-c.csv', index = False, header=True) 
