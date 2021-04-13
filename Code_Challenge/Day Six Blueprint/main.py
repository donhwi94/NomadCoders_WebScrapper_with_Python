import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency
import locale

countries = []

# 국가 리스트 추출
def get_list(rows):
  for row in rows:
    country = row.find_all('td');
    name = country[0].string
    code = country[2].string

    if country[1].string != "No universal currency":
      dict = {"name" : name.capitalize(), "code" : code}
      countries.append(dict)

# 국가 선택
def choose():
  try:
    choice = int(input("\n#: "))
    if choice >= 0 and choice < len(countries):
      country = countries[choice]
      print(f"{country['name']}\n")

      return choice
    else:
      print("Choose a number from the list.")
      choose()
  except:
    print("That wasn't a number.\n")
    choose()

# 환전
def convert(one_code, another_code, amount):
  url = f"https://wise.com/gb/currency-converter/{one_code}-to-{another_code}-rate?amount={amount}"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  default = soup.find('span', {"class":"text-success"}).string
  
  result = format_currency(float(amount)*float(default), another_code, locale="ko_KR")
  amount = format_currency(amount, one_code, locale="ko_KR")
  

  print(f"{amount} is {result}")


# 환전할 금액
def ask(one, another):
  one_country = countries[one]
  another_country = countries[another]
  print(f"How many {one_country['code']} do you want to convert to {another_country['code']}?")
  
  try:
    amount = int(input())
  except:
    print("That wasn't a number.\n")
    ask(one, another)

  convert(one_country['code'], another_country['code'], amount)


def main():
  os.system("clear")
  url = "https://www.iban.com/currency-codes"
  print("Welcome to CurrencyConvert PRO 2000\n")

  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")

  rows = soup.find("tbody").find_all("tr")
  get_list(rows)

  for index, country in enumerate(countries):
    print(f"# {index} {country['name']}")


main()

print("\nWhere are you from? Choose a country by number.")
one = choose()
print("Now choose another country")
another = choose()

ask(one, another)


"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""