from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
result=[]
driver=webdriver.Chrome('C:/Users/X-Note/bigdata/wepPageCrawl/dynamic/wepDriver/chromedriver.exe')
driver.get('https://www.starbucks.co.kr/store/store_map.do?disp=locale')
time.sleep(2)

loca=driver.find_element_by_class_name("loca_search")
loca.click()
time.sleep(2)
sido=driver.find_element_by_class_name('sido_arae_box')
li=sido.find_elements_by_tag_name('li')
li[1].click()
time.sleep(1)

gugun=driver.find_element_by_class_name('gugun_arae_box')
li=gugun.find_elements_by_tag_name('li')
li[14].click()
time.sleep(2)

source=driver.page_source

bs=BeautifulSoup(source,'lxml')
entire=bs.find('ul',class_='quickSearchResultBoxSidoGugun')
starbucksGangnam_list=entire.find_all('li')

print("매장 수: ", len(starbucksGangnam_list))
for stores in starbucksGangnam_list:
    print("매장명: ",stores.find('strong').text,"매장주소:",stores.find('p').text)
    result.append([stores.find('strong').text]+[stores.find('p').text])

CB_tbi=pd.DataFrame(result, columns=('매장명','매장주소'))
CB_tbi.to_csv('C:/Users/X-NOTE/bigdata/wepPageCrawl/dynamic/Starbucks.csv', encoding='cp949', mode='w', index=True)