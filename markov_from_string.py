from markov_python.cc_markov import MarkovChain

text = "There is therefore now no condemnation for those who are in Christ Jesus."
mc = MarkovChain()

mc.add_string(text)
final = mc.generate_text()

print final
 