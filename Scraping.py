import mechanize
from bs4 import BeautifulSoup
import urllib.request
import http.cookiejar

cj = http.cookiejar.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("https://www.topannonces.fr/")

br.select_form(nr=0)
br.form['username'] = 'username'
br.form['password'] = 'password'
br.submit()

print(br.response().read())
