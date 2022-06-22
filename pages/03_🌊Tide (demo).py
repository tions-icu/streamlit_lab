import streamlit as st
import pandas as pd
from datetime import datetime
import pandas as pd
from datetime import time as tm
import plotly.express as px

def tide2():

  default_time1 = tm(0,0)
  default_time2 = tm(23,59)
  

  with st.sidebar:
    st.markdown("---")
    st.title("Measured Tide Level")
    st.markdown("---")
    a1, a2 = st.columns(2)
    with a1:
      Start_Date = st.date_input("Start Date")
      Start_Time = st.time_input('Start Time', default_time1)
    with a2:
      End_Date = st.date_input("End Date")
      End_Time = st.time_input('End Time',  default_time2)
    

  
  ds=datetime.combine(Start_Date,Start_Time)
  de=datetime.combine(End_Date,End_Time)

  inv = st.sidebar.slider("Sampling Interval (min)", min_value=10, max_value=120, value = 60, step = 10)
  ind=pd.date_range(ds, de, freq=str(inv)+'min')
  timestamp=[a.strftime('%Y%m%d-%H%M') for a in ind]

  url="https://api.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fdata.weather.gov.hk%2FweatherAPI%2Fhko_data%2Ftide%2FALL_en.csv&time="#20220613-0000

  tide_df=pd.DataFrame(columns=["Quarry Bay", "Shek Pik", "Tsim Bei Tsui", "Tai Mui Wan", "Tai Po Kau", "Tai O"])
  st.sidebar.markdown("---")
  st.sidebar.write("Loading Progress:")
  p_bar = st.sidebar.progress(0)
  success = st.sidebar.empty()
  out_plot = st.empty()
  output = st.empty()
  
  output.write(tide_df) 
  i=0
  for t in timestamp:
    read_url=url+t
    df = pd.read_csv(url+t)
    success.success("%s was read!"%(url+t))
    #AgGrid(df, height=300,fit_columns_on_grid_load=True)
    df=df.set_index("Tide Station")
    combined_time=df["Date"][0]+" "+df["Time"][0]
    df=df[df.applymap(isnumber)]
    data=df["Height(m)"].to_list()
    read_time=datetime.strptime(combined_time, "%Y-%m-%d %H:%M")
    tide_df.loc[read_time,:]=data
    fig = px.line(tide_df, labels={
                     "variable": "Tide Station",
                     "index": "Time",
                     "value": "Measured Tide Level (mCD)",
                 })
    fig.update_layout(autotypenumbers='convert types', width=1200, height=600)
    out_plot.plotly_chart(fig)
    output.write(tide_df.astype(str)) 
    i+=1
    progress=i/len(timestamp)
    p_bar.progress(progress)
  
  
  
  st.write("Data Source: https://data.gov.hk/en-data/dataset/hk-hko-rss-latest-tidal-info")

def isnumber(x):
    try:
        float(x)
        return True
    except:
        return False

tide2()