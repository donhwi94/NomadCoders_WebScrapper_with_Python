from flask import Flask, render_template, request, redirect, send_file
from so import get_jobs as so_get_jobs
from id import get_jobs as id_get_jobs
from exporter import save_to_file

app = Flask("SuperScrapper")

# fake DB 만들기 
# 라우트의 바깥에 있어야 한다 
# DB에 저장해놓으면 사용자가 같은 단어를 검색했을때, 스크래퍼를 다시 돌릴 필요없이 DB에 있는 데이터를 보여주면 된다
db = {}

@app.route("/")
def home():
  return render_template("home.html")

#  return "<h1>Job Search</h1><form><input placeholder='What job do you want?' required/><button>Search</button>"

# URL의 ?뒤 부터는 query argumets 이다 
@app.route("/report")
def report():
  word = request.args.get('word')
  # 사용자가 단어를 입력하면 그 단어는 소문자로 바꿔주고, 단어를 입력하지 않으면 home으로 리다이렉트한다
  if word:
    word = word.lower() # formating
    
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    else:
      jobs = id_get_jobs(word) + so_get_jobs(word) 
      db[word] = jobs
  else:
    return redirect("/")
  return render_template("report.html", searchingBy=word, resultsNumber=len(jobs), jobs=jobs) # html 파일에서 {{}}은 rendering

# csv 파일로 다운로드하기
@app.route("/export")
def export():
  try:
    word = request.args.get('word')
    if not word:
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    save_to_file(jobs)
    return send_file("jobs.csv")
  except:
    return redirect("/")

app.run(host="0.0.0.0")
