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

print len(function_data)
with jsonlines.open("./multinli_0.9_matched_dev_gram_functionword_swap_pertubed.jsonl", mode='w') as writer:
    writer.write_all(function_data)
    writer.close()

