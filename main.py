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


map = folium.Map(location=[40.34, -110.08], zoom_start=5, tiles="Stamen Terrain")


# FeatureGroup is added to add all of the child markers in it. 



# zip() allows you to iterate over multiple lists at the same time. 

for lat, lng, fac_name, fac_add, fac_city, fac_state, fac_zip, tel_phone in zip(latitude, longitude, facility_name, facility_address, city, state, zipcode, phone_num):
    fg_ensign_location = folium.FeatureGroup(name=str(fac_name), show=True)
    full_add = str(fac_add) + " " + str(fac_city) + " " + str(fac_state) + " " + str(fac_zip)
    html = '''<body style="background-color:Lavender;"><p><strong>'''+ str(fac_name)+'''</strong></p>
    <p>Phone: ''' + str(tel_phone)+ '''</p>
    <p>Address: <a href="http://maps.google.com/?q=''' +str(full_add)+ '''" target="_blank" rel="noreferrer noopener"> ''' +str(full_add)+'''</p></body></a>'''

    iframe = folium.IFrame(html,width=200,height=120)

    popup = folium.Popup(iframe)

    fg_ensign_location.add_child(folium.Marker(location=[lat, lng], popup=popup, icon=folium.Icon(color="blue", icon='glyphicon glyphicon-plus-sign')))


    map.add_child(fg_ensign_location)
folium.LayerControl().add_to(map)
map.save("ensignmap.html")

