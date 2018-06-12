import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pickle
from pycorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP("http://localhost:9000")

premises = pickle.load(open("poss_good_premises.pkl", "rb"))

ner_premises = []
for num, premise in enumerate(premises):
	text = (str(premise))
	print num
	output = nlp.annotate(text, properties={'annotators':'ssplit,tokenize,pos,ner', 'outputFormat':'json'})
	for word in output['sentences'][0]['tokens']:
		if word['ner'] in ['LOCATION', 'PERSON', 'ORGANIZATION']:
			ner_premises.append(premise)
			break
print len(ner_premises)
pickle.dump(ner_premises, open("ner_premises.pkl", "wb"))
