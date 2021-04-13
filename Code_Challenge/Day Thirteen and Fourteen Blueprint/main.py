import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, send_file, redirect
from wwr import get_jobs as wwr_get_jobs
from ro import get_jobs as ro_get_jobs
from so import get_jobs as so_get_jobs
from exporter import save_to_file

"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

app = Flask("donhwi")
db = {}

@app.route("/")
def home():
  jobs = []
  word = request.args.get('word')
  if word:
    word = word.lower()
    print(word)
    existingjobs = db.get(word)
    if existingjobs:
      print("DB에 존재합니다")
      jobs = existingjobs
    else:
      try:
        jobs = wwr_get_jobs(word) + ro_get_jobs(word) + so_get_jobs(word)
        db[word] = jobs
      except:
        print(word, "는 올바르지 않은 키워드입니다.")
        return redirect("/")

  return render_template("index.html", word=word, jobs=jobs, resultsNumber=len(jobs))

@app.route("/export")
def export():
  try:
    word = request.args.get('word')
    jobs = db.get(word)
    save_to_file(jobs)
    return send_file("jobs.csv") 
  except:
    return redirect("/")

app.run(host="0.0.0.0")