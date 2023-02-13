#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from plotly import __version__
get_ipython().run_line_magic('matplotlib', 'qt')
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

init_notebook_mode(connected=True)
cf.go_offline()
oportunitis = pd.read_csv('oportunidades_homework.csv')
ColumnOrigen = oportunitis['origen']
org_counts = ColumnOrigen.value_counts()
origenes = ColumnOrigen.unique()
value_org = np.array(org_counts)
df_origenes = pd.DataFrame(value_org, index=origenes, columns=['Valores'])
df_origenes = df_origenes.reset_index()
grafic_origenes = df_origenes.iplot(kind='pie', labels='index', values='Valores')

