
# coding: utf-8

# # Ellastichoney analysis
# ## Subtitle

# In[31]:

get_ipython().magic(u'matplotlib inline')
import json
file_name = 'elastichoney_logs.json'


# In[40]:

import pandas as pd
from pandas.io.json import json_normalize
file = open(file_name)
data = json.loads(file.read())
json_normalize(data)


# In[38]:

norm_data = json_normalize(data[:])
df = pandas.DataFrame(norm_data)
df.hist()
list(df.columns.values)
#norm_data


# In[18]:

import vincent
vincent.core.initialize_notebook()
world_countries = city_names
geo_data = [{'name': 'countries',
             'url': 'https://github.com/wrobstory/vincent_map_data/blob/master/world-countries.topo.json',
             'feature': 'world-countries'}]
world = vincent.Map(geo_data=geo_data, scale=200)
world.display()
#world.geo_data(projection='winkel3', scale=200, world=world_countries)
#world.to_json(path)


# In[ ]:



