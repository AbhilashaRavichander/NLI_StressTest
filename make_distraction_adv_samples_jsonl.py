import data_preprocessing as dp
import json
import re
import copy

data = dp.load_nli_data(sys.argv[1])
data.sort(key=lambda x:x["sentence1"])
#train_data = train_data[:1000]
#dev_data = dp.load_nli_data("multinli_0.9_dev_mismatched.jsonl")
#test_data = dp.load_nli_data("multinli_0.9_dev_matched.jsonl")
#old_train_data = copy.deepcopy(train_data)
#print old_train_data[0]

def construct_adv(datasets):
    """
    Annotate datasets with feature vectors. Adding right-sided padding.
    """
    addition = sys.argv[3]
    for i, dataset in enumerate(datasets):
        for example in dataset:
            '''Possible ends of sentences: ., !, ?
            u'sentence2': u'I hated the Cinderella story.',
            u'sentence2_binary_parse': u'( I ( ( hated ( the ( Cinderella story ) ) ) . ) )',
            u'sentence2_parse': u'(ROOT (S (NP (PRP I)) (VP (VBZ hated) (NP (DT the) (NNP Cinderella) (NN story))) (. .)))'''
            parts = re.compile("([.!?][\s)]+)").split(example["sentence2_binary_parse"])
            if len(parts) == 1:
                example["sentence2"] = example["sentence2"] + addition
                example["sentence2_binary_parse"] = example["sentence2_binary_parse"] + addition
                example["sentence2_parse"] = example["sentence2_parse"] + addition
            else:
                example["sentence2_binary_parse"] = parts[0] + addition + parts[1]
                #print example["sentence2"]
                sent_parts = re.compile("([.!?][\s]*)").split(example["sentence2"])
                if len(sent_parts) == 1:
                    example["sentence2"] = example["sentence2"] + addition
                else:
                    example["sentence2"] = sent_parts[0] + addition + sent_parts[1]
                parse_parts = example["sentence2_parse"].split("(. .)))")
                if len(parse_parts)>1:
                    example["sentence2_parse"] = parse_parts[0]+ addition +"(. .)))"
                parse_parts = example["sentence2_parse"].split("(. !)))")
                if len(parse_parts)>1:
                    example["sentence2_parse"] = parse_parts[0]+ addition +"(. !)))"
                parse_parts = example["sentence2_parse"].split("(. ?)))")
                if len(parse_parts)>1:
                    example["sentence2_parse"] = parse_parts[0]+ addition +"(. ?)))"


construct_adv([data])
#construct_adv([test_data])
#print old_train_data[0]
fp = open(sys.argv[2], "wb")
for example in data:
	fp.write(json.dumps(example)+"\n")
#fp_2 = open("./multinli_0.9_length_mismatch_matched.jsonl", "wb")
#for example in test_data:
#	fp_2.write(json.dumps(example)+"\n")
#json.dump(dev_data, fp)
#json.dump(test_data,fp_2)

fp.close()
#fp_2.close()
#fp = open("./false_negation_mismatched_control.json", "r")
#adv_data_mismatched = json.load(fp)
#import pdb
#pdb.set_trace()


