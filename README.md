# NLI_StressTest

This repository contains all resources related to the paper "Stress Test Evaluation for Natural Language Inference". For more information, visit https://abhilasharavichander.github.io/NLI_StressTest/

This repository contains the code used to automatically generate word overlap, negation, length mismatch, antonym, noise and numerical reasoning stress tests as described in the paper [insert citation]

## How to Run

Files:
1. make_negation_control_adv_samples_jsonl.py: This file generates the word overlap, negation and length mismatch tests
2. gen_num_test.py, quant_ner.py: These files are used to perform the preprocessing steps (such as splitting word problems into sentences, removing sentences with long rationales and removing sentences which do not contain named entities) and create a set of useful premise sentences for the quantitative reasoning stress test
3. quant_example_gen.py: This file uses the set of useful premise sentences generated after preprocessing to create entailed, contradictory and neutral hypotheses for the quantitative reasoning stress test

How to run the code:
1. python make_negation_control_adv_samples_jsonl.py <sentence to be appended> <input file> <output file> ( this file needs the data_preprocessing.py file provided by MultiNLI creators to run)
2. python gen_num_test.py <input file> <output file>, python quant_ner.py
3. python quant_example_gen.py

The generated stress tests are also available at: https://abhilasharavichander.github.io/NLI_StressTest/


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
