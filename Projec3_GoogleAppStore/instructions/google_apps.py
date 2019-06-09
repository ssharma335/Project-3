#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


android_app=pd.read_csv("googleplaystore.csv")
android_app.head()


# In[3]:


android_app.dtypes


# # Transform the Android Table

# In[4]:


android=android_app[['App','Reviews','Rating','Genres','Installs']]
android.head()


# In[5]:


android=android.dropna()


# In[7]:


#Sort by the name, and observed that there are duplicated apps being rated multiple times i.e same names appears multiple times with the same or different reviews and ratings
android=android.sort_values("App")
#Trim the spaces of all the columns, covert all columns to a string datatype at this point
android['App']=android['App'].str.strip()
android['Reviews']=android['Reviews'].str.strip()
android['Rating']=android['Rating'].astype(str).str.strip()
android['Genres']=android['Genres'].str.strip()
android['Installs']=android['Installs'].str.strip()
#Change the app name case to a lower case prepare for the further duplicates removal
android['App']=android['App'].str.lower()


# In[8]:


#The methodology is if there are duplicated names, we want to take the best reviews and ratings as the result of this app 
#so we created two extra columns and groupby app names to store the max review and ratings
android[['Reviews_max', 'Ratings_max']]=android.groupby('App')['Reviews', 'Rating'].transform('max')
android.head(5)


# In[9]:


#and then we use the max review and ratings as the new review columns and rating columns and prepare for the duplicate removal
new_android=android[['App','Reviews_max','Ratings_max','Genres','Installs']]
new_android.head(5)


# In[10]:


android_table=new_android.drop_duplicates().reset_index(drop=True)
android_table.head(5)


# In[13]:


android_table=android_table.rename(columns={"App":"App Name","Reviews_max":"Total_Reviews","Ratings_max":"Ratings"})


# In[14]:


android_table.head(5)


# In[12]:


#Convert the numerical fields to a number and found the 3.0M gave us an error
#android_table['Ratings']=pd.to_numeric(android_table['Ratings'])
#android_table['Total_Reviews']=pd.to_numeric(android_table['Total_Reviews'])


# In[15]:


#To fix that, we need to change 3.0M to 3,000,000
android_table.loc[android_table.Total_Reviews=='3.0M','Total_Reviews']=3000000


# In[16]:


#now we are happy
android_table['Total_Reviews']=pd.to_numeric(android_table['Total_Reviews'])


# In[17]:


#Check the data type, it looks awesome!
android_table.dtypes


# In[18]:


android_table.head()


# In[19]:


#get_ipython().run_line_magic('timeit', '(android_table["Installs"]).str.replace(\'+\',\'\')')


# In[20]:


android_table.head()


# In[21]:


# cleaning the table
final= android_table.sort_values(["Total_Reviews","Ratings"], ascending=False).reset_index(drop=True)


# In[22]:


final.head()


# In[23]:


final['App Name']=final['App Name'].str.title()
final.head()
x=final[['App Name']].head(10)
y=final[['Total_Reviews']].head(10)
x=x.values.tolist()
y=y.values.tolist()


# In[22]:


#from bs4 import BeautifulSoup
#import requests


# In[23]:


#url ='https://www.makeuseof.com/tag/most-popular-android-apps/'
#response = requests.get(url)
#soup = BeautifulSoup(response.text,'html.parser')
#print(soup.prettify())


# In[44]:


#results = soup.find_all('h2')
#appnames=[]
#for result in results:
#    title= result.text;
#    appnames.append(title)


# In[66]:


#dic={"Popular_Apps":appnames}
#print (dic)
#popularApp=pd.DataFrame(dic)

#popularApp.head()


# In[59]:


#popularApp.drop([0]).head(10)
#df.iloc[:, [0]]
#x=y=[];
#x,y = zip(*(s.split(".") for s in popularApp.drop([0])))
#print (x)


# In[30]:


#export_csv=final.to_csv("datagoogle.csv")
from flask import Flask, flash, redirect, render_template, request, session, jsonify, Markup, abort

app = Flask(__name__)


# In[52]:


#taking mean of ratings.
#Ratings_df = app_overall[['Ratings_x', 'Ratings_y']].mean(axis=1)


# In[31]:


@app.route('/pin')
def loaded():
  #dat=jsonText
  #return “Hello”
  return render_template("google.html",dat=x, mat=y)

if __name__ == "__main__":
  app.run(debug=True)


# In[29]:


#add a column for best reviews 
#app_overall['Best_Reviews'] = Reviews_df


# In[30]:


#add a column for best rating
#app_overall['Best Ratings'] =Ratings_df


# In[31]:


#app_overall.head()


# In[32]:



#clean_tab = app_overall.drop(['Total_Reviews_x','Total_Reviews_y','Ratings_x','Ratings_y','Genres_y'],axis=1)


# In[33]:


#clean_tab.head()


# In[34]:


#rename the column for genress
#final=clean_tab.rename(columns={"Genres_x":"Genres"})


# In[35]:


#final.head()


# In[ ]:




