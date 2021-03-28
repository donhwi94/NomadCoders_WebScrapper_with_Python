import requests
from bs4 import BeautifulSoup

LIMIT = 10
URL = f"https://kr.indeed.com/jobs?q=python&l=%EB%8C%80%EA%B5%AC&limit={LIMIT}"


# 마지막 페이지를 추출하는 함수
def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')

    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]

    return max_page


# 채용 공고에서 채용 직무와 회사명, 회사 위치 가져오는 함수
def extract_job(html):
    #  title = result.find("h2", {"class":"title"}) # 각 채용공고에서 title을 가져온다
    #  anchor = title.find('a')["title"]
    # 위 두개 코드 합치기
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    company_anchor = company.find('a')

    # 회사명에 링크가 걸려있는 경우도 있고 없는경우도 있다
    if company.find('a') is not None:
        company = company_anchor.string
    else:
        company = company.string
    
    #  location = html.find("span", {"class":"location"}).string
    # 이것도 가능하지만, 재택근무가 가능한 형태의 경우 위치 정보가 없어서 .string에서 오류가 나기도 한다
    # div 안에도 attribute로 위치 정보가 있으므로 이걸로 추출
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]

    job_id = html["data-jk"] # 지원하기 링크를 가져오기 위한 id 추출 
    #print(job_id)

    return {
        'title': title,
        'company': company,
        'location': location,
        'link': f"https://kr.indeed.com/%EC%B1%84%EC%9A%A9%EB%B3%B4%EA%B8%B0?jk={job_id}&tk=1f1n85pj4pql0800&from=serp&vjs=3"
    }


# 존재하는 페이지의 url을 만들고 request 하여 각 페이지의 채용 공고를 가져오는 함수
def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
      #print(f"=====Scrapping page {page}=====")
      result = requests.get(f"{URL}&start={page*LIMIT}")
      soup = BeautifulSoup(result.text, "html.parser")
      results = soup.find_all(
          "div", {"class": "jobsearch-SerpJobCard"})  # 각 페이지에 있는 채용 공고를 가져온다

      for result in results:
        job = extract_job(result)
        jobs.append(job)

    return jobs


def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)

  return jobs 