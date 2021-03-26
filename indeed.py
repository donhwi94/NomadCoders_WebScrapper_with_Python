import requests
from bs4 import BeautifulSoup

LIMIT = 10
URL = f"https://kr.indeed.com/jobs?q=python&l=%EB%8C%80%EA%B5%AC&limit={LIMIT}"

# 마지막 페이지를 추출하는 함수이다 
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

# 존재하는 페이지의 url을 만들고, 채용 직무와 회사명 가져오기 
def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser") 
    results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"}) # 각 페이지에 있는 채용 공고를 가져온다

    for result in results:
    #  title = result.find("h2", {"class":"title"}) # 각 채용공고에서 title을 가져온다
    #  anchor = title.find('a')["title"]
    # 위 두개 코드 합치기 
      title = result.find("h2", {"class":"title"}).find("a")["title"]
      company = result.find("span", {"class":"company"})
      company_anchor = company.find('a')
      
      # 회사에 링크가 걸려있는 경우도 있고 없는경우도 있다
      if company.find('a') is not None:
        company = company_anchor.string
      else:
        company = company.string

      print(title, company)
  
  return jobs