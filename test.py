import pandas as pd
import folium

data = pd.read_csv("finaladdressmapV1.csv", encoding= 'unicode_escape')

m = folium.Map(location=[-25, 133], zoom_start=4)

case_num = 34608484848

html = '''<body style="background-color:pink;"><p style="color:red;">Australia</p>
<p>Cases:''' + str(case_num)+ '''</p>
<p>New Cases: +131</p></body>'''

iframe = folium.IFrame(html,width=200,height=120)

popup = folium.Popup(iframe)

marker = folium.Marker([-25.274398, 133.775136],popup=popup).add_to(m)


m.save("test.html")