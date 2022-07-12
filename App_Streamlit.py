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
 
 st.subheader('#Cases registered against Police under Human Rights violations from 2001 to 2010')
 
 g3 = pd.DataFrame(police_hr.groupby(['Year'])['Cases_Registered_under_Human_Rights_Violations'].sum().reset_index())
 g3.columns = ['Year','Cases Registered']
 fig = px.bar(g3,x='Year',y='Cases Registered',color_discrete_sequence=['green'])
 st.write(fig)
 st.caption('- In **2008**, highest number of cases were recorded - **506**')
 st.caption('- The year **2006** recorded **least** number of cases i.e **58**')
 
 st.subheader('#Cases registered against Police under Human Rights violations from 2001 to 2010')
 
 #Cases Registed under Human Rights Violation -  Fake encounter killings
 fake_enc_df = police_hr[police_hr['Group_Name']=='HR_Fake encounter killings'] 
 fake_enc_df.Cases_Registered_under_Human_Rights_Violations.sum()
 
 #Cases Registed under Human Rights Violation -  False implication
 false_imp_df = police_hr[police_hr['Group_Name']=='HR_False implication'] 
 false_imp_df.Cases_Registered_under_Human_Rights_Violations.sum()
 
 g4 = pd.DataFrame(police_hr.groupby(['Year'])['Policemen_Chargesheeted','Policemen_Convicted'].sum().reset_index())

 year=['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010']

 fig = go.Figure(data=[
    go.Bar(name='Policemen Chargesheeted', x=year, y=g4['Policemen_Chargesheeted'],
           marker_color='purple'),
    go.Bar(name='Policemen Convicted', x=year, y=g4['Policemen_Convicted'],
          marker_color='red')])

 fig.update_layout(barmode='group',xaxis_title='Year',yaxis_title='Number of policemen')
 st.write(fig)
 
 st.caption('- In 2009, **69.87%** of policemen have been convicted - highest of the decade')
 st.caption('-For about **three** consecutive years, **2005, 2006, 2007** there has been **no** conviction of policemen')
 
 st.subheader('****Auto Theft cases****')
 auto_theft_traced = auto_theft['Auto_Theft_Coordinated/Traced'].sum()
 auto_theft_recovered = auto_theft['Auto_Theft_Recovered'].sum()
 auto_theft_stolen = auto_theft['Auto_Theft_Stolen'].sum()
 vehicle_group = ['Vehicles Stolen','Vehicles Traced','Vehicles Recovered']
 vehicle_vals = [auto_theft_stolen,auto_theft_traced,auto_theft_recovered]
 colors = ['crimson','gold','green']
 fig = go.Figure(data=[go.Pie(labels=vehicle_group, values=vehicle_vals,sort=False,marker=dict(colors=colors),textfont_size=12)])
 st.write(fig)
 st.caption('Out of **2,467,182** vehicles stolen, **21.2%** have been recovered')
 
 st.subheader('****Year wise vehicles stolen****')
 g5 = pd.DataFrame(auto_theft.groupby(['Year'])['Auto_Theft_Stolen'].sum().reset_index())
 g5.columns = ['Year','Vehicles Stolen']
 fig = px.bar(g5,x='Year',y='Vehicles Stolen',color_discrete_sequence=['#DC143C'])
 st.write(fig)
 st.caption('Seems to be **linear** growth of vehicles stolen')
 
 st.subheader('****# Conclusion****')
 st.caption('Despite governments best effort the number of atrocities and hurt cases are increasing over the years. **Rajasthan ,Uttarpradesh , Bihar ,Maharashtra and Rajasthan** seem to be hotspot for crimes against Scs.')
except:
 st.error("Please select proper file")
 st.stop()
