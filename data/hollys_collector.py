from bs4 import BeautifulSoup
import requests
import csv
import datetime
result=[]

def hollys_process():
  url = 'https://www.hollys.co.kr/store/korea/korStore2.do' # 웹버전
  header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
  res = requests.get(url, headers=header)

  soup = BeautifulSoup(res.text, 'html.parser')
  tag_body = soup.find('tbody')

  for store in tag_body.find_all('tr') :
      if len(store)<=3 :
          break

      store_id = store.select_one('td.noline.center_t').text

      store_area = store.select_one('td.center_t a').text

      store_open = store.find('td', class_='center_t tdp0').text

      store_address = store.select_one('td:nth-of-type(4) > a').text   
      print(store_address)

      result.append([store_id]+[store_area]+[store_open]+[store_address])

def hollys_save(filename):
  fields=['stored_id','store_area','sotre_open','store_address']

  with open(filename,'w',newline='',encoding='cp949') as f: 
    write = csv.writer(f)
    write.writerow(fields) 
    write.writerows(result)
  print("저장완료")
  del result[:]

def hollys_load(filename):
  #            이 값은 외부에서 처리를 해야한다.
  with open(filename,'r',encoding='cp949') as f:
    reader = csv.reader(f)
    for row in reader:
      for cell in row:
        print(cell, end=",")
      print()  

def main():
  hollys_process()
  # to_now=datetime.datetime.today()
  to_now=datetime.datetime.now()
  to_now = to_now.strftime('%Y-%m-%d %H:%M:%s')
  print(to_now)
  filename='./%s-hollys.csv' % to_now
  hollys_save(filename)

if __name__=='__main__':
  main()
