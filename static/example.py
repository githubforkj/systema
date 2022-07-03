import pandas as pd
import folium
from folium.plugins import HeatMap
import webbrowser
import psycopg2 as pg

def map():
        f_map=folium.Map(
                location=[35.658099, 139.741357],
                zoom_start = 10)
        #folium.Marker(location=[35.681167, 139.767052]).add_to(f_map)
        conn =  pg.connect("dbname=postgres user=postgres password='postgres'")
        sql = "select lon, lat from test;"
        df = pd.read_sql_query(sql, conn)
        conn = None
        geo_list=df.values.tolist()
        for i in geo_list:
                folium.Marker(location=i).add_to(f_map)
        #for i in geo_list:
        #        folium.CircleMarker(location=i,radius=40,fill_color='#0000ff').add_to(f_map)
        f_map.save('map.html')
        

if __name__=="__main__":
        map()
