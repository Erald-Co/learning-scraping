
# Import required package (bs4 and requests)
import bs4
import requests

# Website that want to be scraped
url = 'https://jadwalsholat.pkpu.or.id/?id=266'

# Get result from requests URL and check it
contents = requests.get(url)
print(contents)
# print(contents.text)

# Make result from requests more visible structurally
response = bs4.BeautifulSoup(contents.text, features="html.parser")
# print(response)

# Get wanted data (today praying time in 5 times and check it)
data_tr = response.find_all('tr', 'table_highlight')

print(data_tr[0])

# Saved and parse data from data_tr
sholat = {}
i = 0
for d in data_tr[0]:
    if i == 1:
        sholat['Subuh'] = d.get_text()
    elif i == 2:
        sholat['Zuhur'] = d.get_text()
    elif i == 3:
        sholat['Ashar'] = d.get_text()
    elif i == 4:
        sholat['Maghrib'] = d.get_text()
    elif i == 5:
        sholat['Isya'] = d.get_text()
    i += 1

# Try to call data from sholat in specific time
print(sholat)
print(sholat['Maghrib'])