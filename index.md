### What is Natural Language Inference?

Natural language inference (NLI) is the task of determining if a natural language hypothesis can be inferred from a given
premise in a justifiable manner. This requires a model to make the 3-way decision of whether a hypothesis is true given the premise (entailment), false given the premise (contradiction), or whether the truth value cannot be determined (neutral). The MultiNLI corpus is a large-scale dataset for Natural Language Inference featuring premise-hypothesis pairs from ten different genres of text. You can learn more about it [here](http://www.nyu.edu/projects/bowman/multinli/), and about the RepEval shared task [here](https://repeval2017.github.io/shared/) which evaluated models that formed sentence-representations on the Natural language Inference task.

### What are Stress Tests for Natural Language Inference?

[Stress testing](https://en.wikipedia.org/wiki/Stress_testing) is a methodology where systems are tested beyond normal operational capacity in order to confirm that intended specifications are being met and identify weaknesses. For Natural Language Inference, our stress tests are large-scale automatically constructed suites of datasets which evaluate systems on a phenomenon-by-phenomenon basis. Each evaluation set focuses on a single phenomenon so as to not introduce confounding factors, thereby providing a testbed for fine-grained evaluation and analysis.

### Why Should I Use Stress Tests?

Stress tests offer sanity checks for Natural Language Inference models. 

### What Stress Tests Do You Currently Support?

We currently support six stress tests : antonymy, numerical reasoning, word overlap, negation, length mismatch and noise.

### Where Can I Find Out More About Stress Tests?

You can find more about our stress tests in our paper [here](link to paper)

## Paper

## Stress Tests

Stress Tests are downloadable [here](https://drive.google.com/open?id=1faGA5pHdu5Co8rFhnXn-6jbBYC2R1dhw).

## Evaluation Script

## Confusion Matrices

Confusion Matrices for experiments described in the paper are available [here](https://drive.google.com/file/d/1SiOZz_VyJO9zPbBDAu6WIN4RVYwj5Q1T/view?usp=sharing) . Confusion matrices are very useful for further insights into types of errors made by systems. 

## Aggregate Statistics of Sentence Encoder Models
(Last Updated: May 31, 2018)

Aggregate classification performance on six-sentence encoder models described in the paper, on MultiNLI Dev and Stress Tests.


![Image](https://preview.ibb.co/bzFV0y/meta_chart_6.png)

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/AbhilashaRavichander/StressTestEvaluation/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out!.
