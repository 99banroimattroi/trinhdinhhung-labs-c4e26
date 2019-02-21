from youtube_dl import YoutubeDL
import pyexcel
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

conn = urlopen(url)

raw_data = conn.read()

content = raw_data.decode("utf8")

soup = BeautifulSoup(content, "html.parser")
table = soup.find("table", id = "tableContent")
td_list = table.find_all("td", "b_r_c")

news_list = []
for i in td_list:
    a = i.string
    news = {"Kết Quả Hoạt Động Kinh Doanh Công Ty Cổ Phần Sữa Việt Nam": a}
    news_list.append(news)

pyexcel.save_as(records=news_list, dest_file_name="Data_table.xls")


