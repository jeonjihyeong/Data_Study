from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime
from selenium import webdriver
import time

def CoffeeBean_store(result):
    CoffeeBean_URL= "https://www.coffeebeankorea.com/store/store.asp"
    wd=webdriver.Chrome("webDriver C:/Users/bigdata/wepPageCrawl/dynamic/wepDriver/chromedriver.exe")

    for i in range(1,300):
        wd.get(CoffeeBean_URL)
        time.sleep(1)
        try:
            wd.execute_script("storePop2(%d)"%i)
            time.sleep(1)
            html=wd.page_source
            soupCB=BeautifulSoup(html,'html.parser')
            store_name_h2=soupCB.select("div.store_txt>h2")
            store_name=store_name_h2[0].string
            print(store_name)
            store_info=soupCB.select("div.store_txt>table.store_table>tbody>tr>td")
            store_address_list=list(store_info[2])
            store_address=store_address_list[0]
            store_phone=store_info[3].string
            result.append([store_name]+[store_address]+[store_phone])
        except:
            continue
    return

def main ():
    result=[]
    print('CoffeeBean store Crawling >>>>>>>>>>>>>>>>>>>')
    CoffeeBean_store(result)

    CB_tbi=pd.DataFrame(result, columns=('store','address','phone'))
    CB_tbi.to_csv('C:/Users/X-NOTE/bigdata/wepPageCrawl/dynamic/CoffeeBean.csv', encoding='cp949', mode='w', index=True)

if __name__=='__main__':
    main()