from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests


url=input('ENTER THE URL :')
driver = webdriver.Chrome("D:\chromedriver_win32\chromedriver.exe")
df=pd.DataFrame(columns=['news_title','news_short_description','news_category'])
driver.get(url)
html = driver.page_source
button=driver.find_element_by_id('load-more-btn')
def parse(html_code):
    global df
    html_code = BeautifulSoup(html_code, "html.parser")
    #main_div=html_code.find('div',{'class':'card-stack'})
    article_title=html_code.find_all('span',{'itemprop':'headline'})
    article_content=html_code.find_all('div',{'itemprop':'articleBody'})
    for i in range(len(article_title)):
        temporary_df = {'news_title': article_title[i].text, 'news_short_description': article_content[i].text,
                            'news_category': url.split('/')[5]}
        df = df.append(temporary_df, ignore_index=True)

myobj={'category':url.split('/')[5],'news_offset':''}
for i in range(0,100):
    print(i)
    if i==0:
        parse(html)
    else:
        html_code=requests.post('https://www.inshorts.com/en/ajax/more_news',json=myobj).json()
        #print(json.dumps(html, indent=4))  # to see it in nice format.
        parse(html_code['html'])
        myobj['news_offset']=html_code['min_news_id']
        button.click()
        driver.implicitly_wait(10000)


print(df)
df.to_csv('data.csv',encoding='utf-8-sig',mode='a',index=False)
driver.close()