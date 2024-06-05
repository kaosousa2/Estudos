import pandas as pd
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

paises = ('Brasil', 'Colômbia',
          'Argentina', 'Peru', 'Venezuela',
          'Chile', 'Equador', 'Bolívia', 'Paraguai', 'Uruguai',)
indice = np.arange(len(paises))
populacao = [0.754, 0.752, 0.842,  0.762,
             0.691, 0.855, 0.740, 0.692,  0.717, 0.809, ]

plt.ticklabel_format(style='plain')

plt.barh(indice, populacao,
        color=["#0df296", "#f20d84", "#0deaf2", "#f20d58", (1.0, 1.0, 1.0, 1.0, )], edgecolor='#2c2128')
plt.yticks(indice, paises, size=7, )


plt.ylabel(
    '(Dez Maiores IDH da America do Sul)')
plt.title(
    ' Maiores IDH America do Sul 2015 ',)
plt.show()


df = pd.read_csv(
    'https://raw.githubusercontent.com/kaosousa2/Estudos/main/idh2015.csv')
fig = go.Figure(data=go.Choropleth(
    locations=df['pais'],
    z=df['IDH'],
    locationmode='country names',
    text=df['pais'],
    hoverinfo='location+z',
    colorscale='Blues',
    colorbar_title="America do Sul - 2015",
))
fig.update_layout(
    title_text='Os Dez principais IDH da América do Sul - Em 2015',
    geo_scope='south america',
)
fig.show()


import plotly.express as px
import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/kaosousa2/Estudos/main/idh2015.csv')


df.columns = ['pais', 'IDH']


country_codes = {
    'Brazil': 'BRA',
    'Colombia': 'COL',
    'Argentina': 'ARG',
    'Peru': 'PER',
    'Venezuela': 'VEN',
    'Chile': 'CHL',
    'Ecuador': 'ECU',
    'Bolivia': 'BOL',
    'Paraguay': 'PRY',
    'Uruguay': 'URY'
}
df['País'] = df['pais'].map(country_codes)


fig = px.scatter_geo(
    df, 
    locations="País", 
    color="IDH",
    hover_name="pais", 
    size="IDH", 
    projection="mercator",
    title="Dez maiores IDH da América do Sul - 2015",
    color_continuous_scale="oranges"
)


fig.update_geos(scope='south america')


fig.show()