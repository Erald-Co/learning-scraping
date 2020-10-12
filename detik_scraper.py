import requests
from bs4 import BeautifulSoup

# Dapetin request dari link
html_doc = requests.get('https://www.detik.com/terpopuler', params={'tag_from':'framebar'})

soup = BeautifulSoup(html_doc.text, "html.parser")

populer_area = soup.find(attrs={'class':'grid-row list-content'})

titles = populer_area.findAll(attrs={'class':'media__title'})

images = populer_area.findAll(attrs={'class':'media__image'})

# find digunakan untuk mendapatkan tag. Tag adalah huruf/kombinasi huruf yang setelah tanda "<" di html.
# for image in images:
#    print(image.find('a').find('img')['src'])

# Mengambil semua link dari image, dengan mengslice menggunakan 'src'
link_image = [image.find('a').find('img')['src'] for image in images]

# Mengambil semua judul dari image dengan mengslice menggunakan 'title'
link_title = [image.find('a').find('img')['title'] for image in images]

# print(titles)
