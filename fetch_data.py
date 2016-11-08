"""This program fetches John Piper sermon transcripts and creates separate text files with clean transcripts"""

from bs4 import BeautifulSoup
import urllib
import os

TAG = 'John Piper, Pastor'

def collect_links():
	no_of_links = int(raw_input("How many sermons would you like to use? "))
	global links
	links =[]
	for i in range(no_of_links):
		links.append(raw_input("Please input link " + str((i + 1)) + ": "))
	return links

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
	collect_links()
	create_text_list(links)
	create_input_text(text_list)
	create_output_text(text_list)
	delete_input_text(text_list)
	filenames(text_list)
	consolidate(filenames)
	delete_output_text(text_list)

#EVERYTHING ABOVE WORKING

def filenames(text_list):
	global filenames
	filenames = []
	for i in range(len(text_list)):
		filenames.append(('sermon_output_' + str(i) + ('.txt')))

def consolidate(file_list):
	with open('sermon_output.txt', 'w') as outfile:
		for fname in file_list:
			with open(fname) as infile:
				for line in infile:
					outfile.write(line)

def delete_output_text(text_list):
	for i in range(len(text_list)):
		os.remove('sermon_output_' + str(i) + '.txt')

fetch_data()
