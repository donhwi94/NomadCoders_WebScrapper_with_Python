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
    url = url.strip().strip("http://")
    url = "http://" + url
    
    try:
      if url.endswith(".com"):
        response = requests.get(url)
        if response.status_code == 200:
          print(f"{url} is up!")
      else:
        url = url.strip("http://")
        print(f"{url} is not a valid URL.")
    except:
      print(f"{url} is down!")

  start = answer()


# 아래 니꼬쌤 코드 

def restart():
  answer = str(input("Do you want to start over? y/n ")).lower()
  if answer == "y" or answer =="n":
    if answer == "n":
        print("k. bye!")
        return
    elif answer == "y":
      main()
  else:
    print("That's not a valid answer")
    restart()


def main():
  os.system('clear')
  print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)")
  urls = str(input()).lower().split(",")
  for url in urls:
    url = url.strip()
    if "." not in url:
      print(url, "is not a valid URL.")
    else:
      if "http" not in url:
        url = f"http://{url}"
      try:
        request = requests.get(url)
        if request.status_code == 200:
          print(url,"is up!")
        else:
          print(url, "is down!")
      except:
          print(url, "is down!")
  restart()


main()