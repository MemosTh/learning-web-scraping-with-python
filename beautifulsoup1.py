from bs4 import BeautifulSoup
from requests import  get
import  pandas as pd

url = 'https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250'
response = get(url)




hltml_soup = BeautifulSoup(response.text, 'html.parser')

type(hltml_soup)


movie_cont = hltml_soup.find_all('td', class_='titleColumn')
print(type(movie_cont))
print(len(movie_cont))

names = []
for i in movie_cont:

    name = i.a.text
    names.append(name)

"""
print('\n'.join(map(str, names)))
"""

test_df = pd.DataFrame({'movies':names})

print(test_df)