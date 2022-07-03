import pandas as pd
import folium
from folium.plugins import HeatMap
import webbrowser
import psycopg2 as pg
class test1():
    def __init__(self):
        self.word = "Hello world."
    def print_word(self):
        return self.word
    def map(self,lat,lon):
        f_map=folium.Map(
                location=[lat,lon],
                zoom_start = 12)
        #folium.Marker(location=[35.681167, 139.767052]).add_to(f_map)
        conn =  pg.connect("dbname=postgres user=postgres password='postgres'")
        sql = "select lon, lat from test;"
        df = pd.read_sql_query(sql, conn)
        conn = None
        geo_list=df.values.tolist()
        for i in geo_list:
                folium.Marker(location=i).add_to(f_map)
        f_map.save('testmap.html')
