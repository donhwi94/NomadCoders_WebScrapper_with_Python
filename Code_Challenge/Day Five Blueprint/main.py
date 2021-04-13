import os
import requests
from bs4 import BeautifulSoup

table = []

def get_list(row):
  row = row.find_all("td")
  for i in range(len(row)):
    row[i] = row[i].string

  if row[1] != "No universal currency":
    table.append(row)

def answer():
  try:
    ans = int(input("#: "))

    if ans >=0 and ans <len(table):
      print(f"You chose {table[ans][0].capitalize()}\nThe currency code is {table[ans][2]}")
    else:
      print("Choose a number from the list.")
      answer()
  except:
    print("That wasn't a number.")
    answer()

def main():
  os.system("clear")
  url = "https://www.iban.com/currency-codes"
  print("Hello! Please choose select a country by number:")

  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")

  row = soup.find("tbody").find("tr")
  get_list(row)

  while row.find_next_sibling():
    row = row.find_next_sibling()
    get_list(row)
  
  for i in range(len(table)):
    print(f"# {i} {table[i][0].capitalize()} ")

  answer()

main()