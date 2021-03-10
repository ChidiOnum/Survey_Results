#!/usr/bin/env python
# coding: utf-8

# In[243]:


# Import Relevant Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[244]:


# Import data files
df_survey = pd.read_csv("survey_results_public.csv")
df_scheme = pd.read_csv("survey_results_schema.csv")
df_africancountries = pd.read_csv("african_countries.csv")
df_africancountries_english = pd.read_csv("anglophone_african_countries.csv")


# In[245]:


# African Countries
africancountries = df_africancountries['Country'].values.tolist()


# In[246]:


#Introduce column to identify African and Non African records
df_survey['Continent'] = df_survey['Country'].apply(lambda x: "Africa" if x in africancountries else "Outside Africa")


# In[247]:


# number of respondents in the survey

total_respondents = df_survey['Respondent'].count()

df_survey_group = df_survey.groupby(['Continent'])['Respondent'].count().reset_index()

df_survey_group['Percentage_Contribution'] = 100 * (df_survey_group['Respondent']/total_respondents)

df_survey_group.plot.bar(x='Continent',y='Percentage_Contribution')


# In[258]:


df_survey_group


# In[248]:


respondents_ratio = df_survey_group.loc[0,"Respondent"]/df_survey_group["Respondent"].sum()

#Question 1: % of total respondents who reported a country within Africa

print("Answer 01. Percentage of respondents who listed an African country is {:.1%} of total survey respondents".format(respondents_ratio) )


# In[249]:


# Anglophone African Countries
africancountries_english = df_africancountries_english['Country'].values.tolist() 


# In[250]:


#Extract records from survey dataset with country in Africa
df_survey_africa = df_survey[df_survey["Continent"] =="Africa"].reset_index(drop=True)

#Introduce a column to show official language - English or Non English
df_survey_africa['Language'] = df_survey_africa['Country'].apply(lambda x: "English" if x in africancountries_english else "Non English")


# In[251]:


#Stats of respondents with country within Africa
df_survey_africa.describe()


# In[252]:


#Question 2: Distribution of African respondents - Respondents per African Country

df_survey_africa_country = df_survey_africa.groupby(['Country'])['Respondent'].count().reset_index()

df_survey_africa_country['Percentage_Contribution'] = (df_survey_africa_country['Respondent']/total_respondents_africa)

df_survey_africa_country.plot.bar(x='Country',y='Percentage_Contribution')


# In[253]:


#Question 3: Determine Characteristics of  African countries with most respondents

Top4_by_contribution = df_survey_africa_country.nlargest(4, columns='Percentage_Contribution').Percentage_Contribution.sum()

Top4_countrynames = df_survey_africa_country.nlargest(4, columns='Percentage_Contribution')['Country'].to_list()

print("Answer 3: Within Africa, the top 4 countries - " + Top4_countrynames[0] + ", " + Top4_countrynames[1] +", " + Top4_countrynames[0] + ", " + Top4_countrynames[0] + " - with over {:.1%} of respondents are English speaking".format(Top4_by_contribution))


# In[262]:


#Question 4: Given that top programming languages have English keywords/phrases, infer likely impact on respondent's career

#Fill Career Statisfaction with Mean
df_survey_africa['CareerSatisfaction'].fillna(value=df_survey_africa['CareerSatisfaction'].mean(), inplace=True)

# Calculate average career statisfaction based on language of respondent
df_survey_africa_lang = df_survey_africa.groupby(['Language'])['CareerSatisfaction'].mean().reset_index()
df_survey_africa_lang


# In[261]:


#df_survey_africa_lang
df_survey_africa_lang.plot.bar(x='Language',y='CareerSatisfaction')


# In[259]:


print("Answer 4: Career satisfaction appears higher in responents from English-speaking countries compared to those from non-English speaking countries")


# In[ ]:




