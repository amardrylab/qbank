import re
import string
import random
from qsource.models import Qbank

class Option:
	def __init__(self, choice, ans):
		self.choice = choice
		self.ans = ans


# Separating text and options and ans from each question
class Mcq:
	def __init__(self, text):
		reg = re.compile(r'(.*)\no\)(.*)\no\)(.*)\no\)(.*)\no\)(.*)\n(\d)')
		fragments = reg.search(text)
		count=1
		self.question = fragments.group(count)
		self.options = []
		count += 1
		while(count <= 5):
			myoption = Option(fragments.group(count), int(fragments.group(6)) == count-1)
			self.options.append(myoption)
			count+=1
			
		
# Separating the chunk of questions containing the text, options and ans
class qp:
	def __init__(self, filename):
		f = open(filename)
		text = f.read()
		reg = re.compile(r'.*\no\).*\no\).*\no\).*\no\).*\n\d')
		fragments = reg.findall(text)
		self.fullset = []
		for elt in fragments:
			mymcq = Mcq(elt)
			self.fullset.append(mymcq)
	def olotpalot(self):
		random.shuffle(self.fullset)
		for elt in x.fullset:
			random.shuffle(elt.options)
				

def loadquestion(filename):
	x=qp(filename)
	#x.olotpalot()
	for elt in x.fullset:
		qbank=Qbank()
		qbank.headline=elt.question
		qbank.option1=elt.options[0].choice
		if elt.options[0].ans:
			qbank.correctoption=1
		qbank.option2=elt.options[1].choice
		if elt.options[1].ans:
			qbank.correctoption=2
		qbank.option3=elt.options[2].choice
		if elt.options[2].ans:
			qbank.correctoption=3
		qbank.option4=elt.options[3].choice
		if elt.options[3].ans:
			qbank.correctoption=4
		qbank.save()
