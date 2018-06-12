import pickle
import json
import numpy as np

premises = pickle.load(open("ner_premises.pkl", "rb"))
examples = []


def get_entailed_hypothesis(tokens, index, number):
	number = str(number)
	new_digit = np.random.randint(1,9)
	old_digit = int(number[0])
	while new_digit == old_digit:
		new_digit = np.random.randint(1,9)
	new_num = str(new_digit)+number[1:]
	new_tokens = []
	if old_digit < new_digit:
		new_tokens = tokens[:index] + ['less than', new_num] + tokens[index+1:]
	else:
		new_tokens = tokens[:index] + ['more than', new_num] + tokens[index+1:]
	return ' '.join(new_tokens)


def get_contradictory_hypothesis(tokens, index, number):
	prob = np.random.binomial(1, 0.5)
	new_tokens = []
	if prob < 0.5:
		number = str(number)
		new_digit = np.random.randint(1,9)
		old_digit = int(number[0])
		while new_digit == old_digit:
			new_digit = np.random.randint(1,9)
		new_num = str(new_digit)+number[1:]
		new_tokens = tokens[:index] + [new_num] + tokens[index+1:]
	else:
		prob2 = np.random.binomial(1, 0.5)
		if prob2 < 0.5:
			new_tokens = tokens[:index] + ['more than', str(number)] + tokens[index+1:]
		else:
			new_tokens = tokens[:index] + ['less than', str(number)] + tokens[index+1:]
	return ' '.join(new_tokens)

#this function was used to make an easier quantitative reasoning test set
'''
def get_neutral_hypothesis(premise):
	curr_ind = premises.index(premise)
	other_ind = np.random.randint(0, len(premises))
	while curr_ind == other_ind:
		other_ind = np.random.randint(0, len(premises))
	return premises[other_ind]
'''

for premise in premises:
	tokens = premise.split()
	for num, token in enumerate(tokens):
		try:
			number = int(token)
			ent_hyp = get_entailed_hypothesis(tokens, num, number)
			cont_hyp = get_contradictory_hypothesis(tokens, num, number)
			break
		except:
			continue
	#neu_hyp = get_neutral_hypothesis(premise)

	ent_example = {}
	cont_example = {}
	neu_example = {}

	ent_example["sentence1"] = premise.replace("\n", " ")
	cont_example["sentence1"] = premise.replace("\n", " ")
	neu_example["sentence1"] = ent_hyp.replace("\n", " ")

	ent_example["sentence2"] = ent_hyp.replace("\n", " ")
	cont_example["sentence2"] = cont_hyp.replace("\n", " ")
	neu_example["sentence2"] = premise.replace("\n", " ")

	ent_example["sentence1_binary_parse"] = premise.replace("\n", " ")
	cont_example["sentence1_binary_parse"] = premise.replace("\n", " ")
	neu_example["sentence1_binary_parse"] = ent_hyp.replace("\n", " ")

	ent_example["sentence2_binary_parse"] = ent_hyp.replace("\n", " ")
	cont_example["sentence2_binary_parse"] = cont_hyp.replace("\n", " ")
	neu_example["sentence2_binary_parse"] = premise.replace("\n", " ")

	ent_example["gold_label"] = "entailment"
	cont_example["gold_label"] = "contradiction"
	neu_example["gold_label"] = "neutral"
	ent_example["genre"] = "facetoface"
	cont_example["genre"] = "facetoface"
	neu_example["genre"] = "facetoface"

	examples += [ent_example, cont_example, neu_example]


out = open("multinli_0.9_quant_test.jsonl","w")
for example in examples:
	out.write(json.dumps(example)+"\n")
