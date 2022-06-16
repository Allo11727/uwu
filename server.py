
from bs4 import BeautifulSoup
import requests
import RPi.GPIO as GPIO
import threading 
#import drivers 
from time import sleep
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')



@app.route('/bitcoin/')
def Interrupcion():
  url = "https://mx.investing.com/crypto/bitcoin/btc-mxn"
  
  r  = requests.get(url)
  
  data = r.text
  
  soup = BeautifulSoup(data, 'lxml')
       
  temp = soup.find_all('span', class_='text-2xl')
  
  precio    = list()
       
  for i in temp:
     precio.append(i.text)
  
  return i.text
  
@app.route('/dolar/')
def Interrupcion2():
  urldol = 'https://mx.investing.com/currencies/usd-mxn'
  
  rdol  = requests.get(urldol)
  
  datadol = rdol.text
  
  soupdol = BeautifulSoup(datadol, 'lxml')
       
  tempdol = soupdol.find_all('span', class_='text-2xl')
  
  preciodol    = list()
       
  for j in tempdol:
     preciodol.append(j.text)
  
  return j.text

@app.route('/temp/')
def Interrupcion3():
  url3 = "https://www.timeanddate.com/weather/mexico/mexico-city"

  r3  = requests.get(url3)
  data3 = r3.text

  soup3 = BeautifulSoup(data3, 'lxml')
  
  temp3 = soup3.find_all('div', class_="h2")
  preciodol    = list()
       
  for j in temp3:
     preciodol.append(j.text)
  
  return j.text

@app.route('/sensa/')
def Interrupcion4():
  url4 = "https://www.timeanddate.com/weather/mexico/mexico-city"

  r4  = requests.get(url4)
  data4 = r4.text

  soup4 = BeautifulSoup(data4, 'lxml')
  
  #temp3 = soup3.find_all('div', class_="h2")
  sTerm4 = soup4.find_all('div', class_="clear")

  preciodol    = list()
       
  for j in sTerm4:
     preciodol.append(j.text)
  
  return j.text


if __name__ == '__main__':
  app.run(debug=True)

