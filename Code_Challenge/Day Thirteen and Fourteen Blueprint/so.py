import requests 
from bs4 import BeautifulSoup

def extract_job(results):
  jobs = []
  for result in results:
    title = result.find('a', {"class":"s-link"})
    if title:
      title = title.string
    company = result.find('h3').find('span')
    if company:
      company = company.get_text().strip()
    url = "https://stackoverflow.com" + result.find('a', {"class":"s-link"})['href']
    if title and company and url:
      jobs.append({"title":title, "company":company, "url":url})

  return jobs

def extract_jobs(url, last_page):
  jobs = []
  for i in range(1,last_page+1):
    print(f"======page={i}==========")
    response = requests.get(url + f"&pg={i}")
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find('div', {"class","listResults"}).find_all("div", {"class":"-job"})

    jobs = jobs + extract_job(results)

  return jobs

def get_last_page(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  last_page = soup.find('div',{"class":"s-pagination"}).find_all('a', {"class":"s-pagination--item"})[-2].get_text().strip()

  return int(last_page)

def get_jobs(word):
  url = f"https://stackoverflow.com/jobs?r=true&q={word}"
  last_page = get_last_page(url)
  jobs = extract_jobs(url, last_page)
  # print("========so=======", len(jobs))
  return jobs