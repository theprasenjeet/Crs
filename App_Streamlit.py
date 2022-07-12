 #importing libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
from matplotlib import cm
import matplotlib
import plotly.graph_objects as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.colors import n_colors
from plotly.subplots import make_subplots
init_notebook_mode(connected=True)
import cufflinks as cf
cf.go_offline()
 
 
 
from IPython.display import HTML,display
import warnings
warnings.filterwarnings("ignore")
import streamlit as st
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)    #THIS LINE IS MOST IMPORTANT AS THIS WILL DISPLAY PLOT ON
 #NOTEBOOK WHILE KERNEL IS RUNNING
 
import warnings
warnings.filterwarnings("ignore")
 
 
 
st.title("HotSpot Visualization Crime")
try:
 uploaded_file = st.file_uploader("20_Victims_of_rape.csv:")
 if uploaded_file is not None:
   victims = pd.read_csv(uploaded_file)
   st.write(victims)
 
 
 uploaded_file = st.file_uploader("35_Human_rights_violation_by_police.csv:")
 if uploaded_file is not None:
   police_hr = pd.read_csv(uploaded_file)
   st.write(police_hr)
 
 uploaded_file = st.file_uploader("30_Auto_theft.csv:")
 if uploaded_file is not None:
   auto_theft = pd.read_csv(uploaded_file)
   st.write(auto_theft)
   
 uploaded_file = st.file_uploader("10_Property_stolen_and_recovered.csv:")
 if uploaded_file is not None:
   prop_theft = pd.read_csv(uploaded_file)
   st.write(prop_theft)
 
 
 st.subheader('#Incest rape cases reported from 2001 to 2010')
  
 inc_victims = victims[victims['Subgroup']=='Victims of Incest Rape']
 g = pd.DataFrame(inc_victims.groupby(['Year'])['Rape_Cases_Reported'].sum().reset_index())
 g.columns = ['Year','Cases Reported']
 fig = px.bar(g,x='Year',y='Cases Reported',color_discrete_sequence=['blue'])
 st.write(fig)
 st.caption('- In **2005**, around **750** cases were reported which is the **highest** number of that decade.- The year **2010** recorded the **lowest** number of cases i.e **288**.')
 
 st.subheader('#Incest rape cases reported from 2001 to 2010')
 
 g1 = pd.DataFrame(inc_victims.groupby(['Area_Name'])['Rape_Cases_Reported'].sum().reset_index())
 g1.columns = ['State/UT','Cases Reported']
 g1.replace(to_replace='Arunachal Pradesh',value='Arunanchal Pradesh',inplace=True)
 shp_gdf = gpd.read_file('https://github.com/theprasenjeet/Crs/blob/main/Indian_States.shp')
 merged = shp_gdf.set_index('st_nm').join(g1.set_index('State/UT'))

 fig, ax = plt.subplots(1, figsize=(10, 10))
 ax.axis('off')
 ax.set_title('State-wise Rape-Cases Reported (2001-2010)',
             fontdict={'fontsize': '15', 'fontweight' : '3'})
 fig = merged.plot(column='Cases Reported', cmap='Reds', linewidth=0.5, ax=ax, edgecolor='0.2',legend=True)
 st.write(fig)

 st.subheader('****# Conclusion****')
 st.caption('Despite governments best effort the number of atrocities and hurt cases are increasing over the years. **Rajasthan ,Uttarpradesh , Bihar ,Maharashtra and Rajasthan** seem to be hotspot for crimes against Scs.')
except:
 st.error("Please select proper file")
 st.stop()
