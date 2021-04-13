import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def extract_job(results):
  jobs = []
  for result in results:
    closed = result.find('span', {"class":"closed"})
    
    if not closed:
      title = result.find('h2',{"itemprop":"title"})
      if title:
        title = title.string
      company = result.find('h3', {"itemprop":"name"})
      if company:
        company = company.string
      url = "https://remoteok.io" + result.find('a', {"itemprop":"url"})['href']
      if title and company and url:
        jobs.append({"title":title, "company":company, "url":url})

  return jobs

def extract_jobs(url):
  response = requests.get(url, headers=headers)
  soup = BeautifulSoup(response.text, "html.parser")

  tables = soup.find("div", {"class":"container"}).find("table", {"id":"jobsboard"}).find_all('tr', {"class":"job"})
  
  jobs = extract_job(tables)

  return jobs

def get_jobs(word):
  url = f"https://remoteok.io/remote-dev+{word}-jobs"
  jobs = extract_jobs(url)
  # print("=======ro======", len(jobs))
  return jobs
