import plotly.plotly as py
import plotly.graph_objs as go

import json

predicted_latitude_list = []
predicted_longitude_list = []
latitude_list = []
longitude_list = []


with open('kalman_test.json', 'r') as f:
    filtered_data = json.load(f)

for element in filtered_data:
    predicted_latitude_list.append(element["predicted_lat"])
    predicted_longitude_list.append(element["predicted_lon"])
    if (element["gps_lat"] and element["gps_lon"]):
        latitude_list.append(element["gps_lat"])
        longitude_list.append(element["gps_lon"]) 

data = [ go.Scattergeo(
        # locationmode = 'USA-states',
        lon = longitude_list,
        lat = latitude_list,
        # text = df['text'],
        mode = 'markers',
        marker = dict( 
            size = 8, 
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            )
        ))]

layout = dict(
        title = 'Most trafficked US airports<br>(Hover for airport names)', 
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5        
        ),
    )

fig = go.Figure(data=data, layout=layout )
py.iplot(fig, filename='d3-airports' )