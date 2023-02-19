
from bs4 import BeautifulSoup
import requests
import datetime
import csv

result =[]

def weatehr_process() :
  header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
  url= "https://www.weather.go.kr/w/obs-climate/land/city-obs.do"

  res = requests.get(url, headers = header)
  soup = BeautifulSoup(res.text, 'html.parser')
  print(type(soup))

  tbody_tag = soup.find('tbody')
  tr_rs_tag = tbody_tag.find_all('tr')
  print(tr_rs_tag[0])

  for tr_tag in tr_rs_tag :
    td_rs_tag = tr_tag.find_all('td')
    city = td_rs_tag[0].string          # 지역
    cur_temp = td_rs_tag[5].string      # 현재기온
    sen_temp = td_rs_tag[7].string      # 체감온도
    result.append([city, cur_temp, sen_temp])


def weatehr_sav(filename):
  fields =['City', 'CurTemp','SenTemp']

  with open('./%s-weather.csv' % filename, 'w',newline='',encoding='cp949') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerow(result)


def weather_load(filename):
  with open('./%s-weather.csv' % filename, 'r',encoding='cp949') as f:
      reader = csv.reader(f)
      for row in reader:
        for cell in row:
          print(cell, end=',')
        print(end='\n')

def main():
  weather_process()

  to_now=datetime.datetime.now()
  to_now = to_now.strftime('%Y-%m-%d %H:%M:%s')

  weatehr_save(to_now)
  weatehr_load(to_now)


if__name__=='__main__' :
  main()
