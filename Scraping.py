import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib ## http.cookiejar in python3

cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("https://www.topannonces.fr/")

br.select_form(nr=0)
br.form['username'] = 'username'
br.form['password'] = 'password'
br.submit()

print(br.response().read()) 