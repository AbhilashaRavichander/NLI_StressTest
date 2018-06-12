import sys
import json
import jsonlines
import data_preprocessing as dp
import numpy as np
import math
import re
import random
import copy
import argparse

'''Types of perturbations: both character swaps and keyboard typos
Content words and function words'''

def tokenize(string):
    string = re.sub(r'\(|\)', '', string)
    return string.lower().split()

def is_all_lower(word):
    all_chars = list(word)
    for each_char in all_chars:
        if each_char.isupper():
            return False
    return True


def perturb_word_swap(word):
    if len(word) == 2:
        new_word = word[::-1]
    else:
        char_ind = int(np.random.uniform(0, len(word) - 1))
        new_word = list(word)
        first_char = new_word[char_ind]
        new_word[char_ind] = new_word[char_ind + 1]
        new_word[char_ind + 1] = first_char
        new_word = "".join(new_word)
    return new_word


def perturb_word_kb(word):
    keyboard_char_dict = {"a": ['s'], "b": ['v', 'n'], "c": ['x', 'v'], "d": ['s', 'f'], "e": ['r', 'w'],
                          "f": ['g', 'd'], "g": ['f', 'h'], "h": ['g', 'j'], "i": ['u', 'o'], "j": ['h', 'k'],
                          "k": ['j', 'l'], "l": ['k'], "m": ['n'], "n": ['m', 'b'], "o": ['i', 'p'], "p": ['o'],
                          "q": ['w'], "r": ['t', 'e'], "s": ['d', 'a'], "t": ['r', 'y'],
                          "u": ['y', 'i'], "v": ['c', 'b'], "w": ['e', 'q'], "x": ['z', 'c'], "y": ['t', 'u'],
                          "z": ['x']}
    if len(word) > 1:
        new_word = list(word)
        acceptable_subs = []
        for ind, each_char in enumerate(new_word):
            if each_char.lower() in keyboard_char_dict.keys():
                acceptable_subs.append(ind)

        if len(acceptable_subs) == 0:
            return None

        char_ind = random.choice(acceptable_subs)

        first_char = new_word[char_ind]

        new_word[char_ind] = random.choice(keyboard_char_dict[first_char.lower()])
        final_new_word = "".join(new_word)
    return final_new_word



samples = []

char_swap = []
key_swap = []
content_data = []
function_data = []

# Load data
parser = argparse.ArgumentParser(description='Directory with MultiNLI datasets')
parser.add_argument('--base_dir', dest='base_dir', help='Directory with MultiNLI datasets')
args = parser.parse_args()
base_dir = args.base_dir
dev_data = dp.load_nli_data(base_dir+"/multinli_0.9_dev_matched.jsonl")
for sample in dev_data:
    # '''Word swaps in hypothesis'''
    # print ("====")
    # print("hypothesis word swap")
    #
    # sentence = [word for word in tokenize(sample["sentence2_binary_parse"]) if
    #             len(word) > 1 and "-" not in word and len(set(list(word))) > 2 and is_all_lower(word)]
    #
    #
    #
    # print tokenize(sample["sentence2_binary_parse"])
    # print(sentence)
    # if len(sentence) > 0:
    #     word = random.choice(sentence)
    #     print(word)
    #
    #     new_word = ""
    #
    #     found_swap = False
    #
    #     attempts = 0
    #     while not found_swap and attempts < 5:
    #         new_sample = copy.deepcopy(sample)
    #         new_word = perturb_word_swap(word)
    #         if word == new_word:
    #             attempts += 1
    #             continue
    #
    #         new_sample["sentence2_binary_parse"] = new_sample["sentence2_binary_parse"].replace(word, new_word, 1)
    #         new_sample["sentence2"] = new_sample["sentence2"].replace(word, new_word, 1)
    #         new_sample["sentence2_parse"] = new_sample["sentence2_parse"].replace(word, new_word, 1)
    #         if new_sample["sentence2"] == sample["sentence2"]:
    #             attempts += 1
    #             continue
    #
    #
    #         if new_sample["gold_label"] not in ["entailment", "neutral", "contradiction"]:
    #             import pdb
    #
    #             pdb.set_trace()
    #
    #         char_swap.append(new_sample)
    #         found_swap = True
    #         # output_file_1.write(json.dumps(new_sample) + "\n")
    #         attempts += 1

        '''Keyboard swaps in hypothesis'''
        keyboard_char_dict = {"a": ['s'], "b": ['v', 'n'], "c": ['x', 'v'], "d": ['s', 'f'], "e": ['r', 'w'],
                              "f": ['g', 'd'], "g": ['f', 'h'], "h": ['g', 'j'], "i": ['u', 'o'], "j": ['h', 'k'],
                              "k": ['j', 'l'], "l": ['k'], "m": ['n'], "n": ['m', 'b'], "o": ['i', 'p'], "p": ['o'],
                              "q": ['w'], "r": ['t', 'e'], "s": ['d', 'a'], "t": ['r', 'y'],
                              "u": ['y', 'i'], "v": ['c', 'b'], "w": ['e', 'q'], "x": ['z', 'c'], "y": ['t', 'u'],
                              "z": ['x']}
        sentence = tokenize(sample["sentence2_binary_parse"])
        new_sample = copy.deepcopy(sample)

        print ("====")
        print("hypothesis keyborard")
        #print(word)

        found_sub = False
        while not found_sub:
            word = random.choice(sentence)
            first_char = ""
            if len(word) > 1:
                new_word = list(word)
                acceptable_subs = []
                for ind, each_char in enumerate(new_word):
                    if each_char in keyboard_char_dict.keys():
                        acceptable_subs.append(ind)
                if len(acceptable_subs) == 0:
                    continue

                char_ind = random.choice(acceptable_subs)

                first_char = new_word[char_ind]

                new_word[char_ind] = random.choice(keyboard_char_dict[first_char])
                final_new_word = "".join(new_word)
                if word[0].upper() + word[1:] in new_sample["sentence2"]:
                    proper_form = word[0].upper() + word[1:]
                    final_new_word_form = final_new_word[0].upper() + final_new_word[1:]
                    new_sample["sentence2_binary_parse"] = new_sample["sentence2_binary_parse"].replace(proper_form,
                                                                                                        final_new_word_form,
                                                                                                        1)
                    new_sample["sentence2"] = new_sample["sentence2"].replace(proper_form, final_new_word_form, 1)
                    new_sample["sentence2_parse"] = new_sample["sentence2_parse"].replace(proper_form, final_new_word_form,
                                                                                          1)
                else:

                    new_sample["sentence2_binary_parse"] = new_sample["sentence2_binary_parse"].replace(word,
                                                                                                        final_new_word, 1)
                    new_sample["sentence2"] = new_sample["sentence2"].replace(word, final_new_word, 1)
                    new_sample["sentence2_parse"] = new_sample["sentence2_parse"].replace(word, final_new_word, 1)
                found_sub = True
                key_swap.append(new_sample)
            # output_file_2.write(json.dumps(new_sample) + "\n")

        # print ("====")
        # print("content words")
        # print(word)
        #
        # '''Content words : Nouns and Adjectives'''
        #
        # content_pos = ['NNP', 'NNS', 'NNP', 'NNPS', 'JJ', 'JJR', 'JJS']
        #
        # new_sample = copy.deepcopy(sample)
        # sentence = sample["sentence2_parse"]
        #
        # pos_tags = re.findall(r'\(.*?\)', sentence)
        # pos_chunks = [(chunk.split("(")[-1].split(")")[0]).split() for chunk in pos_tags]
        #
        # print(pos_chunks)
        # acceptable_words = []
        # for each_chunk in pos_chunks:
        #     if each_chunk[0] in content_pos:
        #         if len(each_chunk[1]) > 1:
        #             acceptable_words.append(each_chunk[1])
        #
        # # found_sub = False
        # # while not found_sub:
        #
        # new_word = None
        # if len(acceptable_words) > 0:
        #
        #     while new_word is None:
        #         word = random.choice(acceptable_words)
        #
        #         perturbation = random.choice([0, 1])
        #         if perturbation == 0:
        #             new_word = perturb_word_swap(word)
        #         else:
        #             new_word = perturb_word_kb(word)
        #
        #     try:
        #         if word[0].upper() + word[1:] in new_sample["sentence2"]:
        #             proper_form = word[0].upper() + word[1:]
        #             new_word_form = new_word[0].upper() + new_word[1:]
        #             new_sample["sentence2_binary_parse"] = new_sample["sentence2_binary_parse"].replace(proper_form,
        #                                                                                                 new_word_form, 1)
        #             new_sample["sentence2"] = new_sample["sentence2"].replace(proper_form, new_word_form, 1)
        #             new_sample["sentence2_parse"] = new_sample["sentence2_parse"].replace(proper_form, new_word_form, 1)
        #         else:
        #
        #             new_sample["sentence2_binary_parse"] = new_sample["sentence2_binary_parse"].replace(word, new_word, 1)
        #             new_sample["sentence2"] = new_sample["sentence2"].replace(word, new_word, 1)
        #             new_sample["sentence2_parse"] = new_sample["sentence2_parse"].replace(word, new_word, 1)
        #     except Exception as e:
        #         import pdb
        #
        #         pdb.set_trace()
        #     content_data.append(new_sample)
        #         # output_file_3.write(json.dumps(new_sample) + "\n")
        #
        # print ("====")
        # print("function words")
        # print(word)
        #
        # '''Function words : prepositions conjunctions, pronouns, articles'''
        # function_pos = ['IN', 'CC', 'DT', 'PRP', 'PRP$', 'WP', 'WP$']
        #
        # new_sample = copy.deepcopy(sample)
        # sentence = sample["sentence2_parse"]
        #
        # pos_tags = re.findall(r'\(.*?\)', sentence)
        # pos_chunks = [(chunk.split("(")[-1].split(")")[0]).split() for chunk in pos_tags]
        #
        # print(pos_chunks)
        # acceptable_words = []
        # for each_chunk in pos_chunks:
        #     if each_chunk[0] in function_pos:
        #         if len(each_chunk[1]) > 1:
        #             acceptable_words.append(each_chunk[1])
        #
        # if len(acceptable_words) > 0:
        #
        #     # found_sub = False
        #     # while not found_sub:
        #
        #
        #     print(acceptable_words)
        #     word = random.choice(acceptable_words)
        #     perturbation = random.choice([0, 1])
        #     print(word)
        #     if perturbation == 0:
        #         new_word = perturb_word_swap(word)
        #     else:
        #         new_word = perturb_word_kb(word)
        #
        #     try:
        #
        #         if word[0].upper() + word[1:] in new_sample["sentence2"]:
        #             proper_form = word[0].upper() + word[1:]
        #             new_word_form = new_word[0].upper() + new_word[1:]
        #             new_sample["sentence2_binary_parse"] = new_sample["sentence2_binary_parse"].replace(proper_form,
        #                                                                                                 new_word_form, 1)
        #             new_sample["sentence2"] = new_sample["sentence2"].replace(proper_form, new_word_form, 1)
        #             new_sample["sentence2_parse"] = new_sample["sentence2_parse"].replace(proper_form, new_word_form, 1)
        #         else:
        #
        #             new_sample["sentence2_binary_parse"] = new_sample["sentence2_binary_parse"].replace(word, new_word, 1)
        #             new_sample["sentence2"] = new_sample["sentence2"].replace(word, new_word, 1)
        #             new_sample["sentence2_parse"] = new_sample["sentence2_parse"].replace(word, new_word, 1)
        #     except Exception as e:
        #         import pdb
        #
        #         pdb.set_trace()
        #     function_data.append(new_sample)
#f = open("debug.txt","w")
#g = open("debug_bparse", "w")
#char_swap = char_swap[2000:3000]
# for each_point in char_swap:
#     f.write(each_point["gold_label"]+"\n")
#     g.write(each_point["sentence2_binary_parse"].encode('ascii', 'ignore')+"\n")
#
#     if each_point["gold_label"] not in ["entailment", "neutral", "contradiction"]:
#         import pdb
#
#         pdb.set_trace()
#     if each_point["sentence2_binary_parse"] == "":
#         import pdb
#
#         pdb.set_trace()
#     if len(tokenize(each_point["sentence2_binary_parse"]))<2:
#         import pdb
#         pdb.set_trace()

# print(len(char_swap))
# with jsonlines.open("./multinli_0.9_dev_gram_swap_matched.jsonl", mode='w') as writer:
#     writer.write_all(char_swap)
#     writer.close()
# with jsonlines.open("./multinli_0.9_mismatched_dev_gram_keyboard.jsonl", mode='w') as writer:
#     writer.write_all(key_swap)
#     writer.close()

print len(function_data)
with jsonlines.open("./multinli_0.9_matched_dev_gram_functionword_swap_pertubed.jsonl", mode='w') as writer:
    writer.write_all(function_data)
    writer.close()
# with jsonlines.open("./multinli_0.9_mismatched_dev_gram_contentword_swap_perturbed.jsonl", mode='w') as writer:
#     writer.write_all(content_data)
#     writer.close()
