# import gmplot package 
import gmplot 
import json

predicted_latitude_list = []
predicted_longitude_list = []
latitude_list = []
longitude_list = []


with open('kalman50.txt', 'r') as f:
    temp = f.readlines()
    # print(temp)

for element in temp:
    element = element.replace('\r\n', '').split(',')
    # print(element)
    predicted_latitude_list.append(float(element[3]))
    predicted_longitude_list.append(float(element[4]))
    if (element[0] and element[1]):
        latitude_list.append(float(element[0]))
        longitude_list.append(float(element[1]))


    
  
# GoogleMapPlotter return Map object 
# Pass the center latitude and 
# center longitude 
gmap1 = gmplot.GoogleMapPlotter(predicted_latitude_list[0],
                                predicted_longitude_list[0], 13 ) 

# scatter method of map object  
# scatter points on the google map 
gmap1.scatter( predicted_latitude_list, predicted_longitude_list, '#FF0000', 
                              size = 0.1, marker = False )

# Plot method Draw a line in 
# between given coordinates 
# gmap1.plot(predicted_latitude_list, predicted_longitude_list,  
#            'cornflowerblue', edge_width = 1.5) 
  

# scatter method of map object  
# scatter points on the google map 
gmap1.scatter( latitude_list, longitude_list, '#0000FF', 
                              size = 0.15, marker = False )

# Plot method Draw a line in 
# between given coordinates 
# gmap2.plot(latitude_list, longitude_list,  
#            'cornflowerblue', edge_width = 1.5) 
  
# Pass the absolute path 
gmap1.draw( "/home/sushils/Documents/kalman/kalman-filter/map_tanu_new.html" )