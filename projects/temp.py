
from bs4 import BeautifulSoup
import requests
import pandas as pd

url ='https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=77ca3bd4-9630-46b7-802a-e58d6c4b8184&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore'
HEADER =({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; BW/1.1; bit.ly/2W6Px8S; 925f85cc43) Chrome/84.0.4147.105 Safari/537.36' , 'Accept-Language':'en-US , en;q=0.5 '})
deals_data_page = requests.get(url,headers=HEADER)
deals_all_data = BeautifulSoup(deals_data_page.text)
deal_links=deals_all_data.find_all('a',attrs={'class':'_1fQZEK'})
# deal_links
links_done=[link.get('href') for link in deal_links]
print(links_done)


product_names = deals_all_data.find_all('div',attrs={'class':'_4rR01T'})
product_names_clear= [data.text.strip() for data in product_names ]
product_names_clear