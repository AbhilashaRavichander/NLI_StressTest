# NLI_StressTest

[Stress testing](https://en.wikipedia.org/wiki/Stress_testing) is a methodology where systems are tested in order to confirm that intended specifications are being met and identify weaknesses.

For Natural Language Inference, our stress tests are large-scale automatically constructed suites of datasets which evaluate systems on a phenomenon-by-phenomenon basis. Each evaluation set focuses on a single phenomenon so as to not introduce confounding factors, thereby providing a testbed for fine-grained evaluation and analysis.

Stress tests for word overlap, negation, length mismatch, antonym, noise and numerical reasoning stress tests as described in the paper [[1]](https://arxiv.org/abs/1806.00692) can directly be downloaded  [here](https://drive.google.com/file/d/1faGA5pHdu5Co8rFhnXn-6jbBYC2R1dhw/view). You can also find other resources related to this work on our [website](https://abhilasharavichander.github.io/NLI_StressTest/). 

This repository contains the code used to automatically generate stress tests for word overlap, negation, length mismatch, antonym, spelling error and numerical reasoning, intended to help generate stress tests for _new_ data. To evaluate your models, please use the generated [stress tests](https://abhilasharavichander.github.io/NLI_StressTest/). 

## Competence Tests
1. gen_num_test.py, quant_ner.py: These files are used to perform the preprocessing steps (such as splitting word problems into sentences, removing sentences with long rationales and removing sentences which do not contain named entities) and create a set of useful premise sentences for the quantitative reasoning stress test
2. quant_example_gen.py: This file uses the set of useful premise sentences generated after preprocessing to create entailed, contradictory and neutral hypotheses for the quantitative reasoning stress test
3. make_antonym_adv_samples.py: This file contains the code to sample sentences from the MultiNLI development set as possible premises and generate contradicting hypotheses.

### How to Run

Numerical Reasoning:
1. Run python gen_num_test.py INPUT_FILE OUTPUT_FILE
2. Run python quant_ner.py
3. Run python quant_example_gen.py

Antonyms
1. Run python make_antonym_adv_samples.py --base_dir MULTINLI_DIRECTORY

## Distraction Tests
1. make_distraction_adv_samples_jsonl.py: This file generates the word overlap, negation and length mismatch tests

### How to Run

How to run the code:
1. Run python make_distraction_adv_samples_jsonl.py TAUTOLOGY_STRING INPUT_FILE OUTPUT_FILE ( this file needs the data_preprocessing.py file provided by MultiNLI creators to run)


## Noise Tests
1. make_grammar_adv_samples_jsonl.py : Noise test, file generates premise-hypothesis pairs with a word perturbed by a keyboard swap spelling error.

### How to Run
1. Run python make_grammar_adv_samples_jsonl.py --base_dir MULTINLI_DIRECTORY 

The generated stress tests are also available at: https://abhilasharavichander.github.io/NLI_StressTest/

## Evaluation Script
If you want to directly evaluate your system on all stress tests at once you can. 
 Usage is as follows-
1. You will need to report your predictions on the test file found [here](https://drive.google.com/file/d/1Gw3YgA63rFMqAEpzDtO0PKFJ3WsHPQ5d/view?usp=sharing)
2. Write out model predictions as "prediction" field for each sample in the evaluation set. (Sample submission files are available as [sample_submission.jsonl](https://drive.google.com/file/d/18r2lb0sU_YmOZ1mRjHdtyFhsfADD4Qje/view?usp=sharing) and [sample_submission.txt](https://drive.google.com/file/d/14MbtSB-G6RZ87hJNX9AS3I5cVSfz7PDh/view?usp=sharing))
3. Run the [evaluation script](https://github.com/AbhilashaRavichander/NLI_StressTest/blob/master/eval.py) with the command
	python eval.py --eval_file SUBMISSION_FILE > REPORT_FILE.txt

Alternatively, you may write your own evaluation function: our script simply evaluates models on classification accuracy for each stress test at once.

## References

Please considering citing [[1]](https://arxiv.org/abs/1806.00692) if using these stress tests to evaluate Natural Language Inference models.

### Stress Test Evaluation for Natural Language Inference (COLING 2018)

[1] A. Naik, A. Ravichander, N. Sadeh, C. Rose, G.Neubig, [*Stress Test Evaluation for Natural Language Inference*](https://arxiv.org/abs/1806.00692)

```
@inproceedings{naik18coling, 
title = {Stress Test Evaluation for Natural Language Inference},
author = {Aakanksha Naik and Abhilasha Ravichander and Norman Sadeh and Carolyn Rose and Graham Neubig}, 
booktitle = {The 27th International Conference on Computational Linguistics (COLING)}, 
address = {Santa Fe, New Mexico, USA},
month = {August},
year = {2018} }
