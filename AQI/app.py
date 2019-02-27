from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

print("====== Chỉ số chất lượng về không khí (AQI) ======\n")

name = input("    Enter a name city: ")

url = "https://wind.waqi.info/nsearch/full/{}?n=4".format(name)

conn = urlopen(url)
raw_data= conn.read() 
html_content = raw_data

dict_content = json.loads(html_content)   
time = dict_content["results"][0]["s"]["t"][0]
location = dict_content["results"][0]["s"]["n"][0]
aqi = dict_content["results"][0]["s"]["a"]

print("="*50)
print("Date - Time: ", time)
print("Location: ", location)
print("AQI: ", aqi)
print("="*50)