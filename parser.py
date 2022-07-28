import requests
from bs4 import BeautifulSoup


url = 'https://www.avito.ru/ulan-ude/kvartiry/prodam/vtorichka-ASgBAQICAUSSA8YQAUDmBxSMUg'
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
'upgrade-insecure-requests': '1'
}
req = requests.get(url + str(1), headers = header, cookies={'mos_id':'CllGx1yOW5nBYizxkxtbAgA=;'})
if req.status_code==200:
    print(req.json())
else:
    print(req.status_code)
    print(req.url)
# response = requests.get(url, headers=headers)
# print(response.status_code)
soup = BeautifulSoup(req.text, "lxml")
news = soup.find_all('div', class_= 'iva-item-content')
nazvanie = []
for news_item in news:
    if news_item.find('h3', class_='title-root') is not None:
        nazvanie.append(news_item.text)
        print (news_item.get_text(strip=True))
