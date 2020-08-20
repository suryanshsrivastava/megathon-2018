
import io
from PIL import Image
import pytesseract
from wand.image import Image as wi
import csv
from collections import Counter
from collections import defaultdict 
import os, operator
import numpy as np

final_list = {}

filenames=[]



a = os.listdir('./resume_samples')
for b in a:
	if b.endswith('pdf')==True:
		filenames.append(b)


print(filenames)


keyword_to_search = input()
keyword_to_search = keyword_to_search.lower()


if keyword_to_search=='web developer':
	keywords_list = ['nodejs','angular','ruby','rails','python','web','app','framework','tester','meteor','express','zend','django','laravel','spring','codeigniter','machine','angelhack','javascript','html','css','ui/ux','developer','http','stack','Unity3D','android','open','source']

def read_file(text):
	#print ("enter")
	words = []
	words_dict = defaultdict(int)
	text = text.lower().replace('\\n',' ')
	#print (text)
	words += text.split(' ')

	for word in words:
		words_dict[word] += 1

	#print(words_dict)    

	return words_dict

for filename in filenames:

	#print ("entering "+filename)

	pdf = wi(filename = str("./resume_samples/"+filename), resolution = 300)
	pdfImage = pdf.convert('jpeg')

	images = []

	for img in pdfImage.sequence:
		imgPage = wi(image = img)
		images.append(imgPage.make_blob('jpeg'))

	recognized_text = []

	for imgBlob in images:
		im = Image.open(io.BytesIO(imgBlob))
		text = pytesseract.image_to_string(im, lang = 'eng')
		recognized_text.append(text)

	#print(recognized_text)


	myFile = open('resume_data.txt', 'w')
	myFile.write(str(recognized_text))



	word_dict = read_file(str(recognized_text))

	
	#print (word_dict[keyword_to_search])
	score = 0
	for k in keywords_list :
		score+=word_dict[k]
	final_list[filename]=score
	#print("score is "+ str(score))

den = 0
for i in final_list.values():
	if i>den:
		den = i

updated_list = {}

for i in final_list.keys():
	updated_list[i] = final_list[i]/(den+3)


scores = sorted(updated_list.items(), key=lambda kv: kv[1],reverse=True)
print (scores)	

op = open('output.txt','w')
op.write(str(scores))
