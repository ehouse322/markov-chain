#runs the project and outputs the text
from markov_python.cc_markov import MarkovChain
import fetch_data

mc = MarkovChain()

mc.add_file("sermon_output.txt")
initial = mc.generate_text()

def convert_to_file(initial):
	sermon_string = ""
	for n in initial:
		sermon_string += (n + " ")
	with open("Markov_Sermon.txt", "w") as f:
		f.write(sermon_string)

convert_to_file(initial)
