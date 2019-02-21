import pyexcel
from urllib.request import urlopen
from bs4 import BeautifulSoup
# 1. Create connection
url = "https://dantri.com.vn"
conn = urlopen(url)
# 2. Download page 
raw_data = conn.read() 
page_content = raw_data.decode("utf8")
# # print(page_content)
with open("dantri.html", "wb") as f:
    f.write(raw_data)

# # 3. Find ROI - ....
# soup = BeautifulSoup(page_content, "html.parser")
# # print(soup.prettify())
# ul = soup.find("ul", "ul1 ulnew")


# # 4. Extract ROI 
# # print(ul.prettify())
# li_list = ul.find_all("li")
# # print(li_list)
# # li = li_list[0]
# # print(li)
# news_list = []
# for li in li_list:
#     h4 = li.h4
#     # print(h4)
#     a = h4.a
#     link = url + a["href"]
#     # print(link)
#     title = a.string 
#     # print(title)
#     news = {
#         "link" : link,
#         "title" : title
#     }
#     news_list.append(news)
# print(news_list)
# 5. Save
# a_list_of_dictionaries = [
#     {
#         "Name": "Beatrice",
#         "Age": 29
#     },
#     {
#         "Name": "Ceri",
#         "Age": 30
#     },
#     {
#         "Name": "Dean",
#         "Age": 26
#     }
# ]
# pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="your_file.xls")