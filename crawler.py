import lxml.html
import pandas as pd
import requests

def GET_URL(key,year):
    if key == 'j':
        type = 'jyusyo'
    elif key == 'g':
        type = 'g1'
    # make URL and get source
    url = 'http://www.jra.go.jp/datafile/seiseki/replay/{}/{}.html'.format(year,type)
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    html = lxml.html.fromstring(response.text)
    # get the number of races
    num = len(html.xpath('//*[@id="contentsBody"]/div[5]/table/tbody/tr'))
    title = './csv/' + type + str(year) + '.csv'
    arr = [] # <- the array to store race names and URLs
    # get URLs and store
    for i in range(1,(num+1)):
        name_xpath = '//*[@id="contentsBody"]/div[5]/table/tbody/tr[{}]/td[2]'.format(i)
        url_xpath = '//*[@id="contentsBody"]/div[5]/table/tbody/tr[{}]/td[8]/a'.format(i)
        name = html.xpath(name_xpath)[0].text_content()
        url = 'http://www.jra.go.jp' + html.xpath(url_xpath)[0].get("href")
        arr.append([name,url])

    # array -> dataframe
    df = pd.DataFrame(arr)
    df.columns = ['name', 'url']
    df.to_csv(title, header=True, index=False)

if __name__ == "__main__":
    GET_URL('j',2018)
    GET_URL('j',2017)
    GET_URL('j',2016)
    GET_URL('g',2018)
    GET_URL('g',2017)
    GET_URL('g',2016)
