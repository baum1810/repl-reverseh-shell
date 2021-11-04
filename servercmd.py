from urllib.parse import quote
import requests
from os import system
def cls():
  system("cls")
link = "your repl link"
while True:
  cls()
  s = input("Command\n> ")
  a = quote(s.encode('utf-8'))
  r = requests.get(f"{link}/{a}")
