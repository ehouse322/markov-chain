#test markov chain text gnerator
from markov_python.cc_markov import MarkovChain
import urllib2 
from bs4 import BeautifulSoup
import os

#testing markov chain from file path
text = urllib2.urlopen('http://www.challies.com/')
html = text.read()
html_soup = BeautifulSoup(html, 'html.parser')
html_soup = (html_soup.get_text())
print html_soup

text_file = open("test_2", "w+")
text_file.write(html_soup)

mc = MarkovChain()

file_path = os.getcwd()
#print file_path
#mc.add_file("%s/test_2" % (file_path))
#final = mc.generate_text()


#print final

text_file.close()

#testing markov chain from string
