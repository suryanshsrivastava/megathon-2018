import cv2
import sys
import pytesseract

def sort_answers(answers, char):
   my_list = [0, 0, 0, 0];
   for i in range(10):
      try:
         if answers[i*7].upper() == char:
            my_list[0] += 1;
         for j in range(3):
            for k in range(1,3):
               if answers[i*7+j*2+k].upper() == char:
                  my_list[j+1] += 1;
      except:
         print("")
   return my_list;

def percent_of_B(A_list, B_list):
   result = [];
   for i in range(len(B_list)):
      percentage = int(round(float(B_list[i]) / (A_list[i] 
                                         + B_list[i])*100));
      result.append(percentage);
   return result;

def extract_personality(B_list):
   result = ""
   if B_list[0] > 50:
      result += "I";
   elif B_list[0] < 50:
      result += "E";
   else:
      result += "X";
   # dimension two: Sensation versus iNtuition (S vs N): what you focus on   
   if B_list[1] < 50:
      result += "S";
   elif B_list[1] > 50:
      result += "N";
   else:
      result += "X";
   # dimension three: Thinking versus Feeling (T vs F): how you interpret what you focus on
   if B_list[2] < 50:
      result += "T";
   elif B_list[2] > 50:
      result += "F";
   else:
      result += "X";
   # dimension four: Judging versus Perceiving (J vs P): how you approach life 
   if B_list[3] < 50:
      result += "J";
   elif B_list[3] > 50:
      result += "P";
   else:
      result += "X";
      
   return result;



print("Please enter your name to start!")
name = input()
print("Hello there! I will be helping you today applying for a job! The available job we have today is a web developer position in Joveo!")
print("Do you wish to start the application procedure? (Y/N)")
choice = input()

if(choice.lower() == 'y'):

	verification = 0
	while(verification != 1):
		print("To proceed with your application we need you to upload one of your IDs (Valid IDs are Passport/License)")
		id_path = input()
		print("Thank you, let me process the picture you uploaded and get back to you")
		name = str(name).lower() 
		config = ('-l eng --oem 1 --psm 3')
		try:
			im = cv2.imread(id_path, cv2.IMREAD_COLOR)

			text = pytesseract.image_to_string(im, config=config)

			if name in text.lower():
				print("Verified! Thank you, let's move to the next step")
				verification = 1
			else:
				print("Not Verified! Please enter a different ID or upload a clearer picture!")
		except:
			print("Please enter a valid image!")

	resume = 0
	while(resume != 1):
		print("To suit you with the best employers, we need to know more about you, can you please upload your Resume/CV")
		resume_path = input()
		resume = 1

	print("Awesome! Let's move on to the final step now")

	print("To provide our employers with the maximum knowledge about the applicants, we recommend you give a personality test, which will be presented to the employer in a report format")
	print("Do you wish to take the test? (Y/N)")
	choice = input()

	if(choice.lower() == 'y'):
		print("Super! We will be providing you with some questions, you have 3 options (A,B,-)")

		print("Please enter your name:")

		answers = ""
		print("""1. At a party do you
		(a) interact with many, including strangers
		(b) interact with a few, known to you""")
		a = input()
		answers += a

		print("""2. Are you more
		(a) realistic than speculative
		(b) speculative than realistic""")
		a = input()
		answers += a

		print("""3. Is it worse to
		(a) have your 'head in the clouds'
		(b) be 'in a rut'""")

		a = input()
		answers += a


		print("""4. Are you more impressed by
		(a) principles
		(b) emotions""")
		a = input()
		answers += a

		print("""5. Are you more drawn towards the
		(a) convincing
		(b) touching""")
		a = input()
		answers += a


		print("""6. Do you prefer to work
		(a) to deadlines
		(b) just 'whenever'""")
		a = input()
		answers += a

		print("""7. Do you tend to choose
		(a) rather carefully
		(b) somewhat impulsively""")
		a = input()
		answers += a


		print("""8. At parties do you
		(a) stay late, with increasing energy
		(b) leave early, with decreased energy""")
		a = input()
		answers += a

		print("""9. Are you more attracted to
		(a) sensible people
		(b) imaginitive people""")
		a = input()
		answers += a

		print("""10. Are you more interested in
		(a) what is actual
		(b) what is possible""")
		a = input()
		answers += a

		print("""11. In judging others are you more swayed by
		(a) laws than circumstances
		(b) circumstances than laws""")
		a = input()
		answers += a

		print("""12. In approaching others is your inclination to be somewhat
		(a) objective
		(b) personal""")
		a = input()
		answers += a

		print("""13. Are you more
		(a) punctual
		(b) leisurely""")
		a = input()
		answers += a

		print("""14. Does it bother you more having things
		(a) incomplete
		(b) completed""")
		a = input()
		answers += a

		print("""15. In your social groups do you
		(a) keep abreast of other's happenings
		(b) get behind on the news""")
		a = input()
		answers += a

		# with open("personality.txt", "w") as f:
		# 	f.write(name + "\n")
		# 	f.write(answers)
		# f.close()
		print("Thank you! We are done with the procedure! Have a nice day ahead!")	

		# input_file = "personality.txt";
		# output_file = "results.txt";
		# fo = open(input_file, "r");
		# fw = open(output_file, "w");
		# content = fo.readlines();
		# names = []
		# personality_test = []
		# for i in range(len(content)):
		#   if i % 2 != 0:
		#      personality_test.append(content[i].rstrip('\n'));
		#   else:
		#      names.append(content[i].rstrip('\n'));
		# ppl_count = 0;
		# while ppl_count < len(names):
		#   A_response = sort_answers(personality_test[ppl_count], 'A');
		#   B_response = sort_answers(personality_test[ppl_count], 'B');
		#   overall_B = percent_of_B(A_response, B_response);
		#   personality = extract_personality(overall_B);
		#   data = names[ppl_count] + ": " + str(overall_B) + " = " + personality  + "\n";
		#   fw.write(data);
		#   ppl_count+= 1;
		# fo.close();	
		# fw.close();	

else:
	print("See ya later")
