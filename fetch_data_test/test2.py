from markov_python.cc_markov import MarkovChain
import urllib2 
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
import os

mc = MarkovChain()
text = urllib2.urlopen("https://www.crummy.com/software/BeautifulSoup/bs4/doc/#parsing-only-part-of-a-document")
html = text.read()
diagnose(read)



#mc.add_string(example)
#new = mc.generate_text()

#print new