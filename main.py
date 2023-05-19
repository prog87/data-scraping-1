import os
import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.flexjobs.com/search?'
# Menganalisa website
# 1. buat paramater dengan variabel params dengan dictionary {}, dan tambahkan pada Var res
params = {
    'search': 'Python Developer',
    'location': 'Manchester, United Kingdom',
    'country': 'United Kingdom'
}
# 2. buat user agent dengan variabel headers dgn dict {}, dan tambahkan pada Var res
headers = {
    'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

res = requests.get(url, params=params, headers=headers)


# mengecek status code
# print(res.status_code)

# 3. buat variabel baru untuk beautifulsoup dan html parser untuk mendapatkan raw html
# soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())
# Scraping Total Pages
# 1. buat fungsi get total page
def get_total_page():
    params = {
        'search': 'Python Developer',
        'location': 'Manchester, United Kingdom',
        'country': 'United Kingdom'
    }

    res = requests.get(url, params=params, headers=headers)

    # buat direktori dengan library OS, import os
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # buat html file dari raw html
    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()

    total_pages = []
    # definisikan soup
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.prettify())
    # masukan tag ul dan class 'pagination'
    pagination = soup.find('ul', class_='pagination')
    # masukan tag li (tidak ada clas)
    pages_numbers = [int(link.text) for link in pagination.find_all('li') if link.text.isdigit()]
    # tambahkan looping dan append
    for page in pages_numbers:
        total_pages.append(page)
    # print(total_pages)
    # mencari nilai halaman tertinggi dengan fungsi max
    total_pages = max(pages_numbers)
    # print(f"{total_pages}")
    # jika sudah dapat nilai tertinggi, maka kita return
    return total_pages


# Scraping job item
# buat fungsi baru get_all_item
def get_all_item():
    # copas params
    params = {
        'search': 'Python Developer',
        'location': 'Manchester, United Kingdom',
        'country': 'United Kingdom'
    }
    # kita buat request dulu dan panggil url lalu masukkan params dan headers
    res = requests.get(url, params=params, headers=headers)

    # cek request for page
    # buat raw html dengan copas with open()
    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()
    # definisikan parsernya
    soup = BeautifulSoup(res.text, 'html.parser')

    # Scrapping proses
    # gunakan find_all untuk banyak item, jika 1 item gunakan find
    contents = soup.find_all('div', 'col-md-12 col-12')
    # print(contents)

    # Pick Item
    # Title
    # Remote
    # place

    jobs_list = []  # list buat nampung data yg dari looping
    # karena sudah didapat find allnya, berarti kita tinggal looping itemnya
    for item in contents:
        title = item.find('a', 'job-title job-link').text
        remote = item.find('span', 'job-tag d-inline-block me-2 mb-1').text
        place = item.find('div', 'col pe-0 job-locations text-truncate').text
        # print(remote)

        # Sorting data hasil scraping
        # gunakan data dictionary
        data_dict = {
            'title': title,
            'remote': remote,
            'place': place
        }
        # print(data_dict)
        jobs_list.append(data_dict)  # kemudian keluar looping
        # jika ingin menjadikan 1 format data kita buat list
        # kita buat list diluar looping

    # cetak data disini
    # print(jobs_list)
    # print('Jumlah Datanya adalah', len(jobs_list))
    # lebih simpel
    # print(f'jumlah data: {len(jobs_list)}')

# Mengolah hasil scraping menjadi json file
# import json

    # writing json file
    # buat direktori json baru
    try:
        os.mkdir('json_result')
    except FileExistsError:
        pass
    # buat file json baru dgn fungsi with
    with open('json_result/job_list.json', 'w+') as json_data:
        json.dump(jobs_list, json_data)
    print('json created')

# untuk menjalankan file kita ketik main
# dan masukkan fungsinya get_total_page()
# untuk menjalankan fungsi yang berbeda dapat diganti sesuai fungsi yg ingin dijalankan
if __name__ == '__main__':
    get_all_item()
