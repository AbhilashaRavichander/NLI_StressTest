import sys
import json
import numpy as np
import math
import re
import random
import pickle

def tokenize(string):
	string = re.sub(r'\(|\)', '', string)
	return string.lower().split()

input_file = open(sys.argv[1], "r")
output_file = open(sys.argv[2], "w")
samples = []
option_list = ['A', 'B', 'C', 'D', 'E']

#filtering on basis of numerical options and rationale-length constraints
#max allowed rationale length = 5
for line in input_file:
	sample = json.loads(line)
	correct = sample['correct']
	correct_index = option_list.index(correct)
	parsed_options = [-float("inf")]*len(option_list)
	for index, option in enumerate(sample['options']):
		data = re.split('[A-Z] \\)',option)
		try:
			num = float(data[1])
			if num > 1:
				parsed_options[index] = num
		except ValueError:
			continue
	correct_num = parsed_options[correct_index]
	if correct_num != -float("inf"):
		rationale_line_count = len(sample["rationale"].split("\n"))
		if rationale_line_count <= 5:
			samples.append(sample)

for sample in samples:
	output_file.write(json.dumps(sample)+"\n")
