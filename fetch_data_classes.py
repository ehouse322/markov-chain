"""This program fetches John Piper sermon transcripts and creates separate text files with clean transcripts"""

from bs4 import BeautifulSoup
import urllib
import os

TAG = 'John Piper, Pastor'
global length

class Pizza:

	def __init__(self):
		self.length = int(raw_input("How many sermons would you like to use? "))

	#def no_of_links(self):
		#length = int(raw_input("How many sermons would you like to use? "))
		#return length

	def create_input_text(self):
		links =[]
		for i in range(self.length):
			links.append(raw_input("Please input link " + str((i + 1)) + ": "))

		text_list = []
		for i in range(self.length):
			link = urllib.urlopen(links[i])
			html = link.read()
			link.close()
			soup = BeautifulSoup(html, 'html.parser')
			soup_text = soup.get_text().encode('ascii', 'ignore')
			text_list.append(soup_text)

		for i in range(self.length):
			with open("sermon_input_" + str(i) + ".txt", "w") as f:
				f.write(text_list[i])

	def create_output_text(self):
		tag_found = False
		for i in range(self.length):
			with open('sermon_input_' + str(i) + '.txt') as in_file:
				with open('sermon_output_' + str(i) + '.txt', 'w') as out_file:
					for line in in_file:
						if not tag_found:
							if line.strip() == TAG:
								tag_found = True
						else:
							out_file.write(line)

	def delete_input_text(self):
		for i in range(self.length):
			os.remove('sermon_input_' + str(i) + '.txt')


	def fetch_data(self):
		self.create_input_text()
		self.create_output_text()
		#self.delete_input_text()
	
p = Pizza()
p.create_input_text()
p.create_output_text()
p.delete_input_text()

