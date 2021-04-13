import requests
from bs4 import BeautifulSoup 

def extract_job(results):
  jobs = []
  for result in results:
    title = result.find('span', {"class":"title"})
    if title:
      title = title.get_text()
    company = result.find('span', {"class":"company"})
    if company:
      company = company.get_text()
    url = "https://weworkremotely.com" + result.find_all('a')[-1]["href"]
    
    if title and company and url:
      jobs.append({"title":title, "company":company, "url":url})

  return jobs

def extract_jobs(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  results = soup.find('section', {"class":"jobs"}).find_all('li')

  jobs = extract_job(results)
  
  return jobs

def get_jobs(word):
  url = f"https://weworkremotely.com/remote-jobs/search?term={word}&region%5B%5D=Anywhere+%28100%25+Remote%29+Only"

  jobs = extract_jobs(url)
  # print("=======wwr========",len(jobs))
  return jobs
