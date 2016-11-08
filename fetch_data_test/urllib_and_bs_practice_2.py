from bs4 import BeautifulSoup
import urllib
import os

links = [raw_input("Please input link 1: "), raw_input("Please input link 2: ")]
#,raw_input("Please input link 3: "), raw_input("Please input link 4: "), raw_input("Please input link 5: ")]

TAG = 'John Piper, Pastor'

#def get_link():
#	global link
#	link = raw_input("Please input link 1: ")


def create_text_list(links):
	global text_list
	text_list = []
	for i in range(len(links)):
		link = urllib.urlopen(links[i])
		html = link.read()
		link.close()
		soup = BeautifulSoup(html, 'html.parser')
		soup_text = soup.get_text().encode('ascii', 'ignore')
		text_list.append(soup_text)
	return text_list

def create_input_text(text_list):
	for i in range(len(text_list)):
		with open("sermon_input_" + str(i) + ".txt", "w") as f:
			f.write(text_list[i])

def create_output_text(text_list):
	tag_found = False
	for i in range(len(text_list)):
		with open('sermon_input_' + str(i) + '.txt') as in_file:
			with open('sermon_output_' + str(i) + '.txt', 'w') as out_file:
				for line in in_file:
					if not tag_found:
						if line.strip() == TAG:
							tag_found = True
					else:
						out_file.write(line)

def delete_input_text(text_list):
	for i in range(len(text_list)):
		os.remove('sermon_input_' + str(i) + '.txt')


def fetch_data():
	create_text_list(links)
	create_input_text(text_list)
	create_output_text(text_list)
	delete_input_text(text_list)

fetch_data()
