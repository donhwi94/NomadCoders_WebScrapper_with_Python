import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]

app = Flask("DayEleven")
db = {}

def export_contents(result, subreddit):
  contents = []

  while result.next_sibling:
    result = result.next_sibling 
    # 광고가 아니면, title, url, votes 추출
    if not result.find('span', {"class","_2oEYZXchPfHwcf9mTMGMg8"}):
      try:
        title = result.find('h3', {"class","_eYtD2XCVieq6emjKBH3m"}).string
        url = result.find('a', {"class":"_13svhQIUZqD9PVzFcLwOKT"})['href']
        votes = result.find('div', {"class":"_1rZYMD_4xY3gRcSS3p8ODO"}).string
        if votes.endswith('k'):
          votes = votes[:-1]
          votes = float(votes) * 1000
        elif votes.endswith('m'):
          votes = votes[:-1]
          votes = float(votes) * 1000000
        
        contents.append({'title':title, 'url':url, 'votes':int(votes), 'channel':subreddit})
      except:
        print("=None Sorry=")

  # print("=======")
  # print(contents)
  return contents

@app.route("/")
def home():
  return render_template("home.html") 

@app.route("/read")
def read():
  contents = []
  checked = []
  for subreddit in subreddits:
    check = request.args.get(subreddit, 'off')
    print(subreddit)
    
    if check == "on":
      checked.append(subreddit) # read.html 상단에서 체크한 목록 출력하기 위한 용도 
      response = requests.get(f"https://www.reddit.com/r/{subreddit}/top/?t=month", headers=headers)
      soup = BeautifulSoup(response.text, "html.parser")
      result = soup.find("div", {"class":"rpBJOHq2PR60pnwJlUyP0"}).find("div")
      
      existingreddit = db.get(subreddit)
      if existingreddit:
        sub_contents = existingreddit
      else: # db에 없으면 추출 
        sub_contents = export_contents(result, subreddit)
        db[subreddit] = sub_contents

      # 선택한 subreddit의 모든 posts
      contents = contents + sub_contents

  # vote순으로 sort
  contents.sort(key=lambda contents:int(contents['votes']))
  
  return render_template("read.html", contents=contents[::-1], checkedreddit=checked)



app.run(host="0.0.0.0")
