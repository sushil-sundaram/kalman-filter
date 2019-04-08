# import gmplot package 
import gmplot 
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
  
# GoogleMapPlotter return Map object 
# Pass the center latitude and 
# center longitude 
gmap1 = gmplot.GoogleMapPlotter(predicted_latitude_list[0],
                                predicted_longitude_list[0], 13 ) 

# scatter method of map object  
# scatter points on the google map 
# gmap1.scatter( latitude_list, longitude_list, '# FF0000', 
                            #   size = 0.5, marker = False ) 
gmap1.scatter( predicted_latitude_list, predicted_longitude_list, '# 0000FF', 
                              size = 0.5, marker = False )

# Plot method Draw a line in 
# between given coordinates 
gmap1.plot(predicted_latitude_list, predicted_longitude_list,  
           'cornflowerblue', edge_width = 2.5) 
  
# Pass the absolute path 
gmap1.draw( "/home/sushils/Documents/kalman/kalman-filter/predicted_map_tanu_new.html" )

# GoogleMapPlotter return Map object 
# Pass the center latitude and 
# center longitude 
gmap2 = gmplot.GoogleMapPlotter(latitude_list[0],
                                longitude_list[0], 13 ) 

# scatter method of map object  
# scatter points on the google map 
# gmap1.scatter( latitude_list, longitude_list, '# FF0000', 
                            #   size = 0.5, marker = False ) 
gmap2.scatter( latitude_list, longitude_list, '# 0000FF', 
                              size = 0.5, marker = False )

# Plot method Draw a line in 
# between given coordinates 
gmap2.plot(latitude_list, longitude_list,  
           'cornflowerblue', edge_width = 2.5) 
  
# Pass the absolute path 
gmap2.draw( "/home/sushils/Documents/kalman/kalman-filter/actual_map_tanu_new.html" )