################################## IMPORTS ####################################

import pandas as pd
import folium


################################## CSV File Data ####################################
data = pd.read_csv("finaladdressmapV1.csv", encoding='unicode_escape')

# Convert each row into a corresponding list. 
facility_name = data.Name.to_list()
facility_address = data.Address.to_list()
city = data.City.to_list()
state = data.State.to_list()
zipcode = data.Zip.to_list()
phone_num = data.Phone.to_list()
latitude = data.Lat.to_list()
longitude = data.Long.to_list()




################################## Folium Map ####################################


map = folium.Map(location=[40.34, -110.08], zoom_start=6)


# FeatureGroup is added to add all of the child markers in it. 
fg_ensign_locations = folium.FeatureGroup(name="Ensign Locations")


# zip() allows you to iterate over multiple lists at the same time. 
# The for loop adds the child icons to the fg FeatureGroup 
for lat, lng, fac_name in zip(latitude, longitude, facility_name):
    fg_ensign_locations.add_child(folium.Marker(location=[lat, lng], popup=str(fac_name), icon=folium.Icon(color="blue", icon='glyphicon glyphicon-plus-sign')))


map.add_child(fg_ensign_locations)
folium.LayerControl().add_to(map)
map.save("ensignmap.html")

