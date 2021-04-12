import requests
from bs4 import BeautifulSoup



# 마지막 페이지 가져오기
def get_last_page(URL):
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class":"s-pagination"}).find_all('a')

  last_page = pages[-2].get_text(strip=True)
  
  return int(last_page)


# 채용 공고에서 채용 직무와 회사명, 회사 위치, 지원 링크 가져오는 함수
def extract_job(html):
  title = html.find("h2", {"class":"mb4"}).find('a')["title"]
#  company = html.find("h3").find('span').get_text(strip=True)
#  location = html.find("h3").find('span', {"class":"fc-black-500"}).get_text(strip=True)
#  위에처럼 그냥 따로 추출해도 되고,

  # find_all('span') 했는데, span 안에 span이 또 있는 경우는 하위 span은 필요없으므로 firstlevel span만 가져오자 -> recursive=False
#  company_row = html.find("h3", {"class":"fc-black-700"}).find_all("span", recursive=False)
#  company = company_row[0]
#  location = company_row[1]

  company, location = html.find("h3", {"class":"fc-black-700"}).find_all("span", recursive=False)
  company = company.get_text(strip=True)
  location = location.get_text(strip=True)
  job_id = html["data-jobid"]

  return {'title':title, 'company':company, 'location':location, "apply_link":f"https://stackoverflow.com/jobs/{job_id}"}


# 존재하는 페이지의 url 생성 후 request하여 각 페이지의 채용 공고를 가져오는 함수
def extract_jobs(last_page, URL):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&pg={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"-job"})

    #print(f"--------{page+1}----------")

    for result in results:
      job = extract_job(result)
      jobs.append(job)

  return jobs
      
    

def get_jobs(word):
  URL = f"https://stackoverflow.com/jobs?q={word}"
  last_page = get_last_page(URL)
  jobs = extract_jobs(last_page, URL)
  return jobs