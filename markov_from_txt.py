from markov_python.cc_markov import MarkovChain
#import fetch_data
import os

mc = MarkovChain()

file_path = os.getcwd()
print file_path
mc.add_file("sermon_output_" + "0" + ".txt")
initial = mc.generate_text()

def convert_to_string(initial):
	sermon_string = ""
	for n in initial:
		sermon_string += (n + " ")
	print sermon_string
	return sermon_string

convert_to_string(initial)

