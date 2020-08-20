import cv2
import sys
import pytesseract
import fastText
import fasttext_pybind as fasttext
import os
import numpy as np

job = {}

print("Hey! Please enter your name to start!")
job['employer_name'] = input()

print("Please enter your company name!")
job['company_name'] =  input()

print("Hello there! I will be helping you today in finding the perfect candidates for required job!")
print("Do you wish to start the procedure? (Y/N)")
choice = input()
if(choice.lower() == 'y'):
	# extracting data from business
	print("What is the job title?") # job title
	job['title'] = input()

	print("To find you the best candidates, we need to know more about your requirements. What are you looking for in a candidate")
	job['description'] = input()
	print("Please wait while we classify your job description into more general classes!")

	categories = {	'Web Developer': 0,
					'Software Developer': 0, 
					'Engineering and Architecture': 0, 
					'Data Science and Analytics': 0, 
					'Design and Creative': 0, 
					'Sales and Marketing': 0, 
					'Accounting and Consulting':0}

	modelName = "fil9.bin"

	inputcat = str(job['title'])
	inputcat_array = np.array(os.popen("echo \"{}\" | fastText/fasttext print-sentence-vectors fastText/result/{}".format(inputcat, modelName)).read().split(" ")[:-1], dtype=float)

	difsimmilarity = {}

	for category in categories.keys():
		cat_array = np.array(os.popen("echo \"{}\" | fastText/fasttext print-sentence-vectors fastText/result/{}".format(category, modelName)).read().split(" ")[:-1], dtype=float)
		difsimmilarity[category] = np.sum(np.abs(cat_array - inputcat_array))
	category_matched = min(difsimmilarity.items(), key=lambda x: x[1])
	job['category'] = category_matched[0]

	print("Your job description fits in {}".format(category_matched[0]))
	print("Do you wish to change the category? (Y/N)")
	choice = input()

	print("Awesome! Let's move on to the final step now")
	print("Please enter the URL for your job post. we'll do the rest :)!")
	url = input()
	print("Now sit back and relax while we rank the best suitors for this position!")

else:
	print("See ya later")

#jobId jobId of the job
#company company
#title title of the job
#description description of the job
#category category of the job
#type type of the job
#sponsored Only ignore
#url url of the job
#valid job is still valid or not
#city city where this job is located
#state state
#country country
#zip zip
#originalUrl Original url where this job was located
#createdAtDate job creation date
#pubDate date at which job was published
#updatedAtDate date at which job was updated
#refNumber refNumber of the job