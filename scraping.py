import pandas as pd
import requests
import re
import lxml.html

# read csv file
csv = './url_csv/jyusyo2018.csv'
urls = pd.read_csv(csv)
num = len(urls)
# for i in range(len(urls)):
# url = urls.iat[i,1]
# GET_DATA(url)
url = urls.iat[0,1]

def GET_DATA_J(year,url):
    # extract race name
    name = re.match('.*/(.*).html',url).group(1)
    # base title
    base = './race_csv/jyusyo' + str(year) + '_' + name
    # make titles of table and info
    title_t = base + '_table.csv'
    title_i = base + '_info.csv'
    # get page source
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    # read html
    df = pd.read_html(response.text)
    table = df[2].drop(['枠','騎手'], axis=1).drop(0)
    # make csv files
    table.to_csv(title_t, header=True, index=False)


#def GET_TABLE(df):
    # extract necessary table
#    table = df[2].drop(['枠','騎手'], axis=1).drop(0)
    # table.columns = [table.iat[0,i] for i in range(len(table.columns))]
    # table = table.drop(0)
#    return table



def GET_INFO(df):
    # extract necessary table
    race_name = df[11].iat[1,2]
    age_limit = df[13].iat[0,0]
    length = df[13].iat[0,1]

html = lxml.html.fromstring(response.text)
title = html.xpath('//*[@id="contentsBody"]/div[2]/div/h3')[0].text
age_limit = html.xpath('//*[@id="contentsBody"]/div[3]/div[1]/div[1]/div[1]')[0].text
length = html.xpath('//*[@id="contentsBody"]/div[3]/div[1]/div[1]/div[1]')[0].text
course = html.xpath('//*[@id="contentsBody"]/div[3]/div[1]/div[1]/div[2]')[0].text
course = html.xpath('//*[@id="contentsBody"]/div[3]/div[1]/div[3]/div[2]/div/div[1]/div')[0].text
