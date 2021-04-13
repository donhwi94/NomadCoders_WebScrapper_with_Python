import os 
import requests

start = True

def answer():

  while True:
    a = input("Do you want to start over? y/n ")
    if a == "n" or a == "N":
      print("K bye!")
      return False
    elif a == "y" or a =="Y":
      os.system('clear')
      return True
    else:
      print("That's not a valid answer.") 

while start:

  print("Welcome to IsItDown.py!")
  print("Please write a URL or URLs you want to check. (separated by comma")

  urls = input().split(",")

  for url in urls:
    url = url.strip()
    if "." not in url:
      print(f"{url} is not a valid URL.")
    else:
      if "http" not in url:
        url = "http://" + url
      try:
        response = requests.get(url)
        if response.status_code == 200:
          print(f"{url} is up!")
        else:
          print(f"{url} is down!")
      except:
        print(f"{url} is down!")

  start = answer()