import glob
import jsonlines
import argparse
import matplotlib.pyplot as plt
import numpy as np
import json

parser = argparse.ArgumentParser(description='Read prediction file to evaluate.')
parser.add_argument('--eval_file', dest='eval', help='File containing predictions')


args = parser.parse_args()

eval_file = args.eval

competence_tests = ["antonym", "quant"]
distraction_tests = ["negation", "wordoverlap", "length_mismatch"]

def generate_report(results_dict, competence_keys, distraction_keys, noise_keys):
	keys = results_dict.keys()
	keys.sort()

	print "===================== COMPETENCE TESTS ===================== "

	for each_key in competence_keys:
		print (each_key.encode('ascii','ignore')).upper().rjust(30)+" "+str(results_dict[each_key]["accuracy"]).rjust(5)

	print "\n===================== DISTRACTION TESTS ===================== "

	for each_key in distraction_keys:
		print (each_key.encode('ascii','ignore')).upper().rjust(30)+" "+str(results_dict[each_key]["accuracy"]).rjust(5)

	print "\n===================== NOISE TESTS =========================== "

	for each_key in noise_keys:
		print (each_key.encode('ascii','ignore')).upper().rjust(30)+" "+str(results_dict[each_key]["accuracy"]).rjust(5)


def plot(results_dict, competence_keys, distraction_keys, noise_keys):
    #print results_dict.keys()
    matched_scores = []
    mismatched_scores = []
    matched_scores.append(results_dict["mnli_dev_matched"]["accuracy"])
    mismatched_scores.append(results_dict["mnli_dev_mismatched"]["accuracy"])
    matched_scores.append(results_dict["antonym_matched"]["accuracy"])
    mismatched_scores.append(results_dict["antonym_mismatched"]["accuracy"])
    matched_scores.append(results_dict["quant_hard"]["accuracy"])
    mismatched_scores.append(0)
    matched_scores.append(results_dict["wordoverlap_matched"]["accuracy"])
    mismatched_scores.append(results_dict["wordoverlap_mismatched"]["accuracy"])
    matched_scores.append(results_dict["negation_matched"]["accuracy"])
    mismatched_scores.append(results_dict["negation_mismatched"]["accuracy"])
    matched_scores.append(results_dict["length_mismatch_matched"]["accuracy"])
    mismatched_scores.append(results_dict["length_mismatch_mismatched"]["accuracy"])
    matched_scores.append(results_dict["dev_gram_contentword_swap_perturbed_matched"]["accuracy"])
    mismatched_scores.append(results_dict["dev_gram_contentword_swap_perturbed_mismatched"]["accuracy"])
    fig, ax = plt.subplots()
    ind = np.arange(7)
    width = 0.35
    pos = range(7)
    pos[2] = ind[2] + width/2
    p1 = ax.bar(pos, matched_scores, width, color='r')
    p2 = ax.bar(ind+width, mismatched_scores, width, color='b')
    p1[2].set_color('b')
    ax.set_title('Model Performance on all Stress Tests')
    ax.set_ylim((0.0, 100.0))
    tick_pos = ind + width / 2
    tick_pos[2] = pos[2]
    ax.set_xticks(tick_pos)
    ax.set_xticklabels(('MultiNLI\n Dev', 'Antonymy', 'Numerical\n Reasoning', 'Word\n Overlap', 'Negation', 'Length\n Mismatch', 'Spelling\n Error'))
    ax.legend((p1[0], p2[0]), ('Matched', 'Mismatched'))
    #plt.show()

    mismatched_scores[2] = matched_scores[2]
    matched_scores = matched_scores[0:2]+matched_scores[3:]
    max_matched = [74.2, 36.4, 58.3, 52.4, 63.7, 68.3]
    max_mismatched = [74.8, 32.8, 31.3, 58.4, 52.2, 65.0, 69.1]
    min_matched = [63.5, 6.3, 47.2, 39.5, 48.2, 51.1]
    min_mismatched = [64.2, 3.6, 21.2, 47.1, 40.0, 47.3, 49.8]
    fig2, ax2 = plt.subplots()
    ind2 = np.arange(6)
    width2 = 0.2
    p21 = ax2.bar(ind2, min_matched, width2, color='r')
    p22 = ax2.bar(ind2+width2, max_matched, width2, color='b')
    p23 = ax2.bar(ind2+(2*width2), matched_scores, width2, color='g')
    ax2.set_title('Comparison of Model Performance to Benchmarked Sentence\n Encoder Models (Matched)')
    ax2.set_ylim((0.0, 100.0))
    tick_pos2 = ind2 + width2
    ax2.set_xticks(tick_pos2)
    ax2.set_xticklabels(('MultiNLI\n Dev', 'Antonymy', 'Word\n Overlap', 'Negation', 'Length\n Mismatch', 'Spelling\n Error'))
    ax2.legend((p21[0], p22[0], p23[0]), ('Min Benchmark Accuracy', 'Max Benchmark Accuracy', 'Your Model Accuracy'))

    fig3, ax3 = plt.subplots()
    ind3 = np.arange(7)
    width3 = 0.2
    p31 = ax3.bar(ind3, min_mismatched, width3, color='r')
    p32 = ax3.bar(ind3+width3, max_mismatched, width3, color='b')
    p33 = ax3.bar(ind3+(2*width3), mismatched_scores, width3, color='g')
    ax3.set_title('Comparison of Model Performance to Benchmarked Sentence\n Encoder Models (Mismatched)')
    ax3.set_ylim((0.0, 100.0))
    tick_pos3 = ind3 + width3
    ax3.set_xticks(tick_pos3)
    ax3.set_xticklabels(('MultiNLI\n Dev', 'Antonymy', 'Numerical\n Reasoning', 'Word\n Overlap', 'Negation', 'Length\n Mismatch', 'Spelling\n Error'))
    ax3.legend((p31[0], p32[0], p33[0]), ('Min Benchmark Accuracy', 'Max Benchmark Accuracy', 'Your Model Accuracy'))
    plt.show()


results_dict = {}
if eval_file.endswith("jsonl"):
    input = open(eval_file)
    for line in input:
        obj = json.loads(line)
	if obj["source"] not in results_dict:
	    results_dict[obj["source"]] = {"total": 0.0, "correct": 0.0, "accuracy": 0.0}
	if obj["prediction"] == obj["gold_label"]:
	    results_dict[obj["source"]]["correct"] += 1
	results_dict[obj["source"]]["total"]+=1

if eval_file.endswith("txt"):
	f = open(eval_file,"r")
	all_lines = f.read().split("\n")


	for each_line in all_lines[1::]:
		if each_line == "":
			break
		parts = each_line.split()
		source = parts[-2]
		pred_label = parts[-1]
		gold_label = parts[0]
		if source not in results_dict:
			results_dict[source] = {"total": 0.0, "correct": 0.0, "accuracy": 0.0}
		if pred_label == gold_label:
			results_dict[source]["correct"] += 1
		results_dict[source]["total"]+=1


for each_key in results_dict:
		results_dict[each_key]["accuracy"] = round(results_dict[each_key]["correct"] * 100.0 / results_dict[each_key]["total"],2)

keys = results_dict.keys()
keys.sort()

competence_keys = []
for each_test in competence_tests:
	for each_key in keys:
		if each_key.startswith(each_test):
			competence_keys.append(each_key)

distraction_keys = []
for each_test in distraction_tests:
	for each_key in keys:
		if each_key.startswith(each_test):
			distraction_keys.append(each_key)

noise_keys = []
for each_key in keys:
	if "gram" in each_key:
		noise_keys.append(each_key)


generate_report(results_dict, competence_keys, distraction_keys, noise_keys)
plot(results_dict, competence_keys, distraction_keys, noise_keys)
