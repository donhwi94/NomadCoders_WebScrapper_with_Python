import requests
import json
from flask import Flask, render_template, request, redirect

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"

# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  return f"{base_url}/items/{id}"

def export_data(data):
  hits = data['hits']
  contents = []
  for hit in hits:
    title = hit['title']
    url = hit['url']
    points = hit['points']
    author = hit['author']
    comments = hit['num_comments']
    objectID = hit['objectID']
    contents.append({'title':title, 'url':url, 'points':points, 'author':author, 'comments':comments, 'objectID':objectID})

  return contents

def export_comments(data):
  comments = []

  for comment in data:
    author = comment['author']
    url = comment['url']
    text = comment['text']
    comments.append({'author':author, 'url':url, 'text':text})

  return comments

  
db = {}
app = Flask("DayNine")

@app.route("/")
def home():
  word = request.args.get('order_by')
  if not word:
    word = "popular"

  word = word.lower()
  if word == "popular":
    response = requests.request("GET", popular, headers={}, data={})
  elif word == "new":
    response = requests.request("GET", new, headers={}, data={})

  # data = response.content
  data = json.loads(response.content)

  existingcontents = db.get(word)
  if existingcontents:
    contents = existingcontents
  else:
    contents = export_data(data)
    db[word] = contents

  return render_template("index.html", order_by=word, contents=contents)

@app.route("/<ID>")
def comment(ID):
  url = make_detail_url(ID)
  response = requests.request("GET", url, headers={}, data={})
  data = json.loads(response.content)

  info = {}
  info['title'] = data['title']
  info['points'] = data['points']
  info['author'] = data['author']
  info['url'] = data['url']

  data = data['children']
  comments = export_comments(data)

  return render_template("detail.html", comments=comments, info=info)


app.run(host="0.0.0.0")