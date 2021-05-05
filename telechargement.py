#!/usr/bin/env python
# coding: utf-8

# In[1]:


from modules.loader import Loader
from modules.splitting_csv import print_nb_row


# # Téléchargement des données

# In[2]:


loader = Loader(
    "https://stdatalake012.blob.core.windows.net/public/brief-12.zip",
    'datas/ZIP/',
    'datas/RAW/'
)
loader.ensure_data_loaded()


# In[ ]:


print_nb_row('datas/RAW/')

