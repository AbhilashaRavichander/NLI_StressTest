'''
Generate Antonym Stress Tests
Requirements: Python 2.7, NLTK Wordnet, NLTK WSD, Jsonlines
Output: antonym_matched.jsonl, antonym_mismatched.jsonl
'''

import data_preprocessing as dp
import json
import re
import copy
from nltk.corpus import wordnet
import nltk
from nltk.tokenize import word_tokenize
from nltk.wsd import lesk
import jsonlines
import argparse

parser = argparse.ArgumentParser(description='Directory with MultiNLI datasets')
parser.add_argument('--base_dir', dest='base_dir', help='Directory with MultiNLI datasets')
args = parser.parse_args()
base_dir = args.base_dir

'''Replace with local paths'''
dev_data = dp.load_nli_data(base_dir + "/multinli_0.9/multinli_0.9_dev_mismatched.jsonl")
test_data = dp.load_nli_data(base_dir + "/multinli_0.9/multinli_0.9_dev_matched.jsonl")

premise_hypothesis_pairs = []


def construct_example(sentence, example, flag):
    all_examples = []
    seen_premise_hypothesis = []

    blacklist_words = ["here", "goodness", "yes", "no", "decision", "growing", "priority", "cheers", "volume", "right",
                       "left", "goods", "addition", "income", "indecision", "there", "parent", "being", "parents",
                       "lord", "lady", "put", "capital", "lowercase", "unions"]
    for num, each_word in enumerate(sentence):
        if each_word not in blacklist_words:
            best_sense = lesk(sentence, each_word)

            if best_sense is not None and (best_sense.pos() == 's' or best_sense.pos() == 'n'):
                for lemma in best_sense.lemmas():
                    possible_antonyms = lemma.antonyms()
                    for antonym in possible_antonyms:
                        if "_" in antonym._name or antonym._name == "civilian":
                            # Spurious antonyms
                            continue

                        new_example = copy.deepcopy(example)

                        # Flag decides if original premise or hypothesis should be used as the premise
                        #  in the antonym stress test
                        if flag == 1:
                            if each_word not in example["sentence1"]:
                                continue
                            new_example["sentence2"] = new_example["sentence1"].replace(each_word, antonym._name, 1)
                            new_example["sentence2_binary_parse"] = new_example["sentence1_binary_parse"].replace(
                                each_word, antonym._name, 1)
                            new_example["sentence2_parse"] = new_example["sentence1_parse"].replace(each_word,
                                                                                                    antonym._name, 1)

                        else:
                            if each_word not in example["sentence2"]:
                                continue
                            new_example["sentence1"] = new_example["sentence2"].replace(each_word, antonym._name, 1)
                            new_example["sentence1_binary_parse"] = new_example["sentence2_binary_parse"].replace(
                                each_word, antonym._name, 1)
                            new_example["sentence1_parse"] = new_example["sentence2_parse"].replace(each_word,
                                                                                                    antonym._name, 1)

                        new_example["gold_label"] == "contradiction"

                        # Logging unique sentence pairs

                        if (new_example["sentence1"], new_example["sentence2"]) in seen_premise_hypothesis:
                            continue
                        else:
                            seen_premise_hypothesis.append((new_example["sentence1"], new_example["sentence2"]))

                        all_examples.append(new_example)
    return all_examples


def tokenize(string):
    string = re.sub(r'\(|\)', '', string)
    return string.lower().split()


def get_antonym_extensions(example):
    sentence_1 = tokenize(example["sentence1_binary_parse"])
    sentence_2 = tokenize(example["sentence2_binary_parse"])
    possible_examples = []

    possible_examples += construct_example(sentence_1, example, 1)
    possible_examples += construct_example(sentence_2, example, 2)
    return possible_examples


def construct_adv(datasets):
    """
    Annotate datasets with feature vectors. Adding right-sided padding.
    """
    all_new_datasets = []
    for i, dataset in enumerate(datasets):

        print "ORIGINAL DATASET"
        print len(dataset)
        new_dataset = []
        for example in dataset:
            '''Possible ends of sentences: ., !, ?
            u'sentence2': u'I hated the Cinderella story.',
            u'sentence2_binary_parse': u'( I ( ( hated ( the ( Cinderella story ) ) ) . ) )',
            u'sentence2_parse': u'(ROOT (S (NP (PRP I)) (VP (VBZ hated) (NP (DT the) (NNP Cinderella) (NN story))) (. .)))'''

            new_dataset.extend(get_antonym_extensions(example))

        final_dataset = []

        premise_hypothesis_pairs = []

        for each_example in new_dataset:
            each_example["gold_label"] = "contradiction"

            if each_example["sentence1"] != each_example["sentence2"]:
                if (each_example["sentence1"], each_example["sentence2"]) not in premise_hypothesis_pairs:
                    premise_hypothesis_pairs.append((each_example["sentence1"], each_example["sentence2"]))
                    final_dataset.append(each_example)
                else:
                    pass

        all_new_datasets.append(final_dataset)

        print "NEW DATASET"
        print len(final_dataset)

    return all_new_datasets


# (dev_data)
all_new_datasets = construct_adv([dev_data, test_data])

fp = open("./antonym_mismatched.json", "wb")
fp_2 = open("./anotnym_matched.json", "wb")
json.dump(all_new_datasets[0], fp)
json.dump(all_new_datasets[1], fp_2)

with jsonlines.open("./multinli_0.9_antonym_mismatched.jsonl", mode='w') as writer:
    writer.write_all(all_new_datasets[0])
    writer.close()

with jsonlines.open("./multinli_0.9_antonym_matched.jsonl", mode='w') as writer:
    writer.write_all(all_new_datasets[1])
    writer.close()
