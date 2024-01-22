#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[4]:


title = str(input('Enter the topic: ')).replace(' ','+')
link = 'https://www.google.com/search?q=' + title + '+wikipedia'

res = requests.get(link)
soup = BeautifulSoup(res.text,'html.parser')


for sp in soup.find_all('div'):
    try:
        link = sp.find('a').get('href')
        if ('en.wikipedia.org' in link):
            break
    except:
        pass
    
link = link[7:].split('&')[0]


# In[6]:


res = requests.get(link)
soup = BeautifulSoup(res.text, 'html.parser')

corpus = ''
for p in soup.find_all('p'):
    corpus += p.text
    corpus += '\n'
    
corpus = corpus.strip()

for i in range (500):
     corpus = corpus.replace('['+str(i)+']', '')


# In[7]:


print (corpus)


# In[ ]:





# In[ ]:




