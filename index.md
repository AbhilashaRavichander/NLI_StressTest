### What is Natural Language Inference?

Natural language inference (NLI) is the task of determining if a natural language hypothesis can be inferred from a given
premise in a justifiable manner. This requires a model to make the 3-way decision of whether a hypothesis is true given the premise (entailment), false given the premise (contradiction), or whether the truth value cannot be determined (neutral).

The MultiNLI corpus is a large-scale dataset for Natural Language Inference featuring premise-hypothesis pairs from ten different genres of text. You can learn more about it [here](http://www.nyu.edu/projects/bowman/multinli/), and about the RepEval shared task [here](https://repeval2017.github.io/shared/) which evaluated models that formed sentence-representations on the Natural Language Inference task.

### What are Stress Tests for Natural Language Inference?

[Stress testing](https://en.wikipedia.org/wiki/Stress_testing) is a methodology where systems are tested beyond normal operational capacity in order to confirm that intended specifications are being met and identify weaknesses.

For Natural Language Inference, our stress tests are large-scale automatically constructed suites of datasets which evaluate systems on a phenomenon-by-phenomenon basis. Each evaluation set focuses on a single phenomenon so as to not introduce confounding factors, thereby providing a testbed for fine-grained evaluation and analysis.

### Why Should I Use Stress Tests?

Stress tests offer sanity checks for Natural Language Inference models. 

Neural models perform well on standard datasets for NLI.  Few “difficult” cases in traditional evaluation can result in an optimistic estimate of model performance. We would like an evaluation that rewards a systems ability to make real inferential decisions instead of pattern-matching behaviour. We would also like to correlate model errors to well-defined phenomena to understand strengths and weaknesses. Stress tests provide such a phenomenon-by-phenomemon evaluation.

We recommend that these stress tests be used to supplement traditional evaluation on the MultiNLI dataset.

### What Stress Tests Do You Currently Support?

We currently support six stress tests : antonymy, numerical reasoning, word overlap, negation, length mismatch and noise.

### Where Can I Find Out More About Stress Tests for Natural Language Inference?

You can find more about our stress tests in our paper [here](https://arxiv.org/abs/1806.00692)

## Paper
Our paper ["Stress Test Evaluation for Natural Language Inference"](https://arxiv.org/abs/1806.00692)

## Stress Tests

Stress Tests are downloadable [here](https://drive.google.com/open?id=1faGA5pHdu5Co8rFhnXn-6jbBYC2R1dhw).

## Evaluation Script

If you want to directly evaluate your system on all stress tests at once you can. 
 Usage is as follows-
1. You will need to report your predictions on the test file found [here](https://drive.google.com/file/d/1hA2ZiAH2mC1U0yolft3Y8Ike-fjHmNmw/view?usp=sharing)
2. Write out model predictions as "prediction" field for each sample in the evaluation set. (Sample submission files are available as [sample_submission.jsonl](https://drive.google.com/file/d/18r2lb0sU_YmOZ1mRjHdtyFhsfADD4Qje/view?usp=sharing))
3. Run the [evaluation script](https://github.com/AbhilashaRavichander/NLI_StressTest/blob/master/eval.py) with the command
	python eval.py --eval_file SUBMISSION_FILE > REPORT_FILE.txt
  

## Confusion Matrices

Confusion Matrices for experiments described in the paper are available [here](https://drive.google.com/file/d/1SiOZz_VyJO9zPbBDAu6WIN4RVYwj5Q1T/view?usp=sharing) . Confusion matrices are very useful for further insights into types of errors made by systems. 

## Performance of Sentence Encoder Models

(Last Updated: May 31, 2018)

Classification performance(%) of SOTA models on stress tests vs. MultiNLI Dev. __Please open a Github issue to be added to the leaderboard__!

### Antonymy

| System        |MultiNLI Dev Matched  | Antonym Matched  |MultiNLI Dev Mismatched  | Antonym Mismatched  |
| ------------- |:-------------:| :-----:|:-------------:| :-----:|
| [(Nie and Bansal, 2017)](http://aclweb.org/anthology/W17-5308)     | 74.2 | 15.1 | 74.8 | 19.3 |
| [(Chen. et al., 2017)](http://aclweb.org/anthology/W17-5307)    |  73.7 | 11.6 | 72.8 | 9.3 |
| [(Balazs. et al., 2017)](http://aclweb.org/anthology/W17-5310)  | 71.3 | 36.4 | 71,6 | 32.8 |
| [(Conneu et al., 2017)](https://github.com/facebookresearch/InferSent)     | 70.3 | 14.4 | 70.6 | 10.2 |
| [BiLSTM](https://www.nyu.edu/projects/bowman/multinli/paper.pdf)     | 70.2 | 13.2 | 70.8 | 9.8 |
| [CBOW](https://www.nyu.edu/projects/bowman/multinli/paper.pdf)     | 63.5 | 6.3 | 64.2 | 3.6 |


### Numerical Reasoning

| System        |MultiNLI Dev Matched  | MultiNLI Dev Mismatched  | Numerical Reasoning  |
| ------------- |:-------------:| :-------------:| :-----:|
| [(Nie and Bansal, 2017)](http://aclweb.org/anthology/W17-5308)     | 74.2 |74.8 | 21.2 |
| [(Chen. et al., 2017)](http://aclweb.org/anthology/W17-5307)    |  73.7 | 72.8 | 30.3 |
| [(Balazs. et al., 2017)](http://aclweb.org/anthology/W17-5310)  | 71.3 | 71,6 | 30.2 |
| [(Conneu et al., 2017)](https://github.com/facebookresearch/InferSent)     | 70.3 | 70.6 | 28.8 |
| [BiLSTM](https://www.nyu.edu/projects/bowman/multinli/paper.pdf)     | 70.2 | 70.8 | 31.3 |
| [CBOW](https://www.nyu.edu/projects/bowman/multinli/paper.pdf)     | 63.5 | 64.2 | 30.3 |



### Word Overlap


| System        |MultiNLI Dev Matched  | Word Overlap Matched  |MultiNLI Dev Mismatched  | Word Overlap Mismatched  |
| ------------- |:-------------:| :-----:|:-------------:| :-----:|
| [(Nie and Bansal, 2017)](http://aclweb.org/anthology/W17-5308)     | 74.2 | 47.2 | 74.8 | 47.1 |
| [(Chen. et al., 2017)](http://aclweb.org/anthology/W17-5307)    |  73.7 | 58.3 | 72.8 | 58.4 |
| [(Balazs. et al., 2017)](http://aclweb.org/anthology/W17-5310)  | 71.3 | 53.7 | 71,6 | 54.4 |
| [(Conneu et al., 2017)](https://github.com/facebookresearch/InferSent)     | 70.3 | 50.0 | 70.6 | 50.2 |
| [BiLSTM](https://www.nyu.edu/projects/bowman/multinli/paper.pdf)     | 70.2 | 57.0 | 70.8 | 58.5 |
| [CBOW](https://www.nyu.edu/projects/bowman/multinli/paper.pdf)     | 63.5 | 53.6 | 64.2 | 55.6 |

### Negation

| System |MultiNLI Dev Matched|Negation Matched|MutliNLI Dev Mismatched|Negation Mismatched| 
|:-------------:|:-------------:|:-----:|:------:|:-------:|
|[(Nie & Bansal, 2017)](http://aclweb.org/anthology/W17-5308)|74.2 | 39.5| 74.8 |40.0|
|[(Chen et al, 2017)](http://aclweb.org/anthology/W17-5307)| 73.7| 52.4| 72.8| 52.2|
| [(Balazs et al, 2017)](http://aclweb.org/anthology/W17-5310) | 71.3 |49.5| 71.6| 50.4|
| [(Conneau et al, 2017)](https://arxiv.org/pdf/1705.02364.pdf)| 70.3| 46.8| 70.6| 46.6| 
|[BiLSTM](http://www.nyu.edu/projects/bowman/multinli/paper.pdf) | 70.2| 51.4| 70.8| 51.9|
| [CBOW](http://www.nyu.edu/projects/bowman/multinli/paper.pdf)| 63.5| 43.7| 64.2| 44.2|

### Length Mismatch

| System |MultiNLI Dev Matched|Length Mismatch Matched|MutliNLI Dev Mismatched|Length Mismatch Mismatched| 
|:-------------:|:-------------:|:-----:|:------:|:-------:|
|[(Nie & Bansal, 2017)](http://aclweb.org/anthology/W17-5308)|74.2 | 48.2| 74.8 |47.3 |
|[(Chen et al, 2017)](http://aclweb.org/anthology/W17-5307)| 73.7| 63.7| 72.8| 65.0|
| [(Balazs et al, 2017)](http://aclweb.org/anthology/W17-5310) | 71.3 |48.6 | 71.6| 49.6|
| [(Conneau et al, 2017)](https://arxiv.org/pdf/1705.02364.pdf)| 70.3| 58.7| 70.6| 59.4| 
|[BiLSTM](http://www.nyu.edu/projects/bowman/multinli/paper.pdf) | 70.2| 49.7| 70.8| 51.2|
| [CBOW](http://www.nyu.edu/projects/bowman/multinli/paper.pdf)| 63.5| 48.0| 64.2| 49.3|

### Spelling Error

| System |MultiNLI Dev Matched|Spelling Error Matched|MutliNLI Dev Mismatched|Spelling Error Mismatched| 
|:-------------:|:-------------:|:-----:|:------:|:-------:|
|[(Nie & Bansal, 2017)](http://aclweb.org/anthology/W17-5308)|74.2 | 51.1 | 74.8 |49.8 |
|[(Chen et al, 2017)](http://aclweb.org/anthology/W17-5307)| 73.7| 68.3| 72.8| 69.1|
| [(Balazs et al, 2017)](http://aclweb.org/anthology/W17-5310) | 71.3 |66.6 | 71.6| 67.0|
| [(Conneau et al, 2017)](https://arxiv.org/pdf/1705.02364.pdf)| 70.3| 58.3| 70.6| 59.4| 
|[BiLSTM](http://www.nyu.edu/projects/bowman/multinli/paper.pdf) | 70.2| 65.0| 70.8| 65.1|
| [CBOW](http://www.nyu.edu/projects/bowman/multinli/paper.pdf)| 63.5| 60.3| 64.2| 60.6|

Aggregate classification performance on six-sentence encoder models described in the paper, on MultiNLI Dev and Stress Tests.


![Image](https://preview.ibb.co/bzFV0y/meta_chart_6.png)

## Citing

If you use these stress tests for NLI research, please consider citing our work as follows:

```
@inproceedings{naik18coling,
    title = {Stress Test Evaluation for Natural Language Inference},
    author = {Aakanksha Naik and Abhilasha Ravichander and Norman Sadeh and Carolyn Rose and Graham Neubig},
    booktitle = {The 27th International Conference on Computational Linguistics (COLING)},
    address = {Santa Fe, New Mexico, USA},
    month = {August},
    year = {2018}
}
```
## Contact

Please get in touch with us for any questions/issues at aravicha@cs.cmu.edu or anaik@cs.cmu.edu .
