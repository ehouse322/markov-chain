from bs4 import BeautifulSoup
import urllib

#raw_input("Please input link 2: ")]
#,raw_input("Please input link 3: "), raw_input("Please input link 4: "), raw_input("Please input link 5: ")]

TAG = 'John Piper, Pastor'

def get_link():
	global link
	link = raw_input("Please input link 1: ")

def create_input_text(link):
	initial = urllib.urlopen(link)
	html = initial.read()
	initial.close()
	soup = BeautifulSoup(html, 'html.parser')
	soup_text = soup.get_text().encode('ascii', 'ignore')
	with open('sermon_input.txt', 'w') as file:
		file.write(soup_text)

def create_output_text():
	tag_found = False
	with open('sermon_input.txt') as in_file:
		with open('sermon_output.txt', 'w') as out_file:
			for line in in_file:
				if not tag_found:
					if line.strip() == TAG:
						tag_found = True
				else:
					out_file.write(line)

def fetch_data():
	get_link()
	create_input_text(link)
	create_output_text()

fetch_data()
