import requests
from bs4 import BeautifulSoup


url = 'http://esstu.ru/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers=headers)
print(response.status_code)
soup = BeautifulSoup(response.text, "lxml")
news = soup.find_all('div', class_= 'bNewsItem')
nazvanie = []
for news_item in news:
    if news_item.find('a', class_='c3') is not None:
        nazvanie.append(news_item.text)
        print (news_item.get_text(strip=True))
