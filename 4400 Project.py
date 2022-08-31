#!/usr/bin/env python
# coding: utf-8

# In[35]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

#scrap the info from the website
year1=2020
url1 ="https://www.basketball-reference.com/leagues/NBA_2020_totals.html"
html=urlopen(url1)
soup = BeautifulSoup(html)

#get the column header
soup.findAll('tr',limit=2)
headers=[th.getText() for th in soup.findAll('tr',limit=2)[0].findAll('th')]

headers = headers[1:]
headers

# avoid the first header row
rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]

stats = pd.DataFrame(player_stats, columns = headers)
stats_select = stats[['Player','Age','GS','TRB','AST','PTS']]
stats_select


# In[37]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

#scrap the info from the website
year2=2019
url2 ="https://www.basketball-reference.com/leagues/NBA_2019_totals.html"
html=urlopen(url2)
soup = BeautifulSoup(html)

#get the column header
soup.findAll('tr',limit=2)
headers=[th.getText() for th in soup.findAll('tr',limit=2)[0].findAll('th')]

headers = headers[1:]
headers

# avoid the first header row
rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]

stats2 = pd.DataFrame(player_stats, columns = headers)
stats_select2 = stats2[['Player','Age','GS','TRB','AST','PTS']]
stats_select2


# In[36]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

#scrap the info from the website
year3=2018
url3 ="https://www.basketball-reference.com/leagues/NBA_2018_totals.html"
html=urlopen(url3)
soup = BeautifulSoup(html)

#get the column header
soup.findAll('tr',limit=2)
headers=[th.getText() for th in soup.findAll('tr',limit=2)[0].findAll('th')]

headers = headers[1:]
headers

# avoid the first header row
rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]

stats3 = pd.DataFrame(player_stats, columns = headers)
stats_select3 = stats3[['Player','Age','GS','TRB','AST','PTS']]
stats_select3


# In[ ]:




