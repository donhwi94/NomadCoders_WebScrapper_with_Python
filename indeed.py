import requests
from bs4 import BeautifulSoup

LIMIT = 10
URL = f"https://kr.indeed.com/jobs?q=python&l=%EB%8C%80%EA%B5%AC&limit={LIMIT}"

# 마지막 페이지를 추출하는 함수 
def extract_indeed_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class":"pagination"})

  links = pagination.find_all('a')

  pages = []
  for link in links[:-1]:
    pages.append(int(link.string))

  max_page = pages[-1]

  return max_page

# 존재하는 페이지의 url을 만드는 함수 
def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&start={page*LIMIT}")

    print(result.status_code)
  
  return jobs