import requests
from bs4 import BeautifulSoup


url = 'https://animego.org/anime/random'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers=headers)
print(response.status_code)
soup = BeautifulSoup(response.content, "html.parser")
nazvanie = soup.find('div', {'class' :'anime-title'}).find('h1')
print ('Аниме: ' + nazvanie.text)
animetyp = soup.find('div', class_= 'anime-info').find_all("dt")
animetyp1 = soup.find('div', class_= 'anime-info').find_all("dd")
print(animetyp[0].text, animetyp1[0].text)
print(animetyp[1].text, animetyp1[1].text)
print(animetyp[5].text, animetyp1[5].text)
# animetyp1 = soup.find('div', class_= 'anime-info').find_all("dt")
# print('Данное аниме \n' + animetyp, animetyp1)
# animetyp1 = soup.find('div', class_= 'anime-info').find('dd')
# print (animetyp1.text)
# nazvanie = []
# for news_item in news:
#     # if news_item.find('h1', class_= '') is not None:
#         # nazvanie.append(news_item.text)
#         print (news_item[0].text)
