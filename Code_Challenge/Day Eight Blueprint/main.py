import os
import csv
import requests
from bs4 import BeautifulSoup

# 각 브랜드별 채용 정보 추출
def export_jobs(brand_url):
  response = requests.get(brand_url)
  soup = BeautifulSoup(response.text, "html.parser")
  results = soup.find('div', {"id":"NormalInfo"}).find('tbody').find_all('tr', {"class":""})
  
  jobs = []
  for result in results:
    place = result.find('td', {"class":"local first"})
    # .get_text()
    if place:
      place = place.get_text()
    title = result.find('td', {"class":"title"}).find('span',{"class":"title"})
    # .get_text()
    if title:
      title = title.get_text()
    j_time = result.find('td', {"class":"data"})
    # .get_text()
    if j_time:
      j_time = j_time.get_text()
    pay = result.find('td', {"class":"pay"})
    # .get_text()
    if pay:
      pay = pay.get_text()
    j_date = result.find('td', {"class":"regDate"})
    # .get_text()
    if j_date:
      j_date = j_date.get_text()
    
    jobs.append({"place":place, "title":title, "time":j_time, "pay":pay, "date":j_date})
  
  return jobs

# CSV 파일로 저장
def save_to_csv(company, brand_jobs):
  file = open(f"{company}.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["place", "title", "time", "pay", "date"])

  for job in brand_jobs:
    writer.writerow(list(job.values()))
  return 


os.system("clear")
alba_url = "http://www.alba.co.kr"

# 슈퍼 브랜드 채용 정보 추출
response = requests.get(alba_url)
soup = BeautifulSoup(response.text, "html.parser")
brands = soup.find('div', {"id":"MainSuperBrand"}).find('ul', {"class":"goodsBox"}).find_all('li')

brand_links = []
for brand in brands:
  brand_link = brand.find('a')['href']
  company = brand.find('span', {"class":"company"}).get_text().replace("/", " ")
  print(company)
  # get_last_page(brand_link)
  brand_jobs = export_jobs(brand_link)
  save_to_csv(company, brand_jobs)
