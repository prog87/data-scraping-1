import requests
from bs4 import BeautifulSoup

url = 'https://www.flexjobs.com/search?'
# Menganalisa website
# 1. buat paramater dengan variabel params dengan dictionary {}, dan tambahkan pada Var res
params = {
    'search':'Python Developer',
    'location': 'Manchester, United Kingdom',
    'country': 'United Kingdom'
}
# 2. buat user agent dengan variabel headers dgn dict {}, dan tambahkan pada Var res
headers = {'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

res = requests.get(url, params=params, headers=headers)
# mengecek status code
# print(res.status_code)

# 3. buat variabel baru untuk beautifulsoup dan html parser untuk mendapatkan raw html
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())


