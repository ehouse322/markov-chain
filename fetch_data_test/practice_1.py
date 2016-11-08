#Fetch data using urllib2

import urllib2
import urllib
from bs4 import BeautifulSoup

response = urllib2.urlopen("http://mlb.mlb.com/home")
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
print (soup.prettify())