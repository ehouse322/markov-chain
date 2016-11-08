from bs4 import BeautifulSoup
import urllib
import string

links = [raw_input("Please input link 1: ")]
#, raw_input("Please input link 2: ") ,raw_input("Please input link 3: "), raw_input("Please input link 4: "), raw_input("Please input link 5: ")]
print links

def get_string(links):
	for i in range(len(links)):
		string_i = ''
		link_i = urllib.urlopen(links[i])
		html_i = link_i.read()
		link_i.close()
		soup_i = BeautifulSoup(html_i, 'html.parser')
		soup_text_i = soup_i.get_text()
		text_i = soup_text_i.encode('ascii', 'ignore')
		print text_i
		return text_i
		with open("sermon_string", "w") as f:
			f.write(sermon_string)

	#with open("text_file_i", "w") as f:
		#f.write("%s") % (text_i)
	#'span style="color:#000000;font-family:Arial;font-size:13px;"')

def write_to_file(sermon_string):
	with open(sermon_string, "w") as f:
		f.write(sermon_string)

get_string(links)

