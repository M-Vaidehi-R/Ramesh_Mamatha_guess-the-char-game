# importing the question dictionary from the questions library
from components.quiz_dictionary import questions
from components import quiz_array, quiz_functions
#import emoji

print ("\n \n WINNIE THE POOH 'guess who' GAME \n \n")
print (" 1) Rules: Think of a main character of your favorite cartoon Winnie the Pooh (answe the questions considering yourself as that character). \n 2) Enter yes or no for the 10 questions asked. \n 3) We will guess the character you thought at the end\n")
print( "Lets get started...  \n \n ")

#print(emoji.emojize(":grinning_face_with_big_eyes:"))

answer1 =  questions["q1"] [input (questions["q1"] ["ques_1"]) ]

quiz_array.quiz_total +=answer1

print("\n")

answer2 =  questions["q2"] [input (questions["q2"] ["ques_2"]) ]

quiz_array.quiz_total +=answer2
print("\n")

answer3 =  questions["q3"] [input (questions["q3"] ["ques_3"]) ]

quiz_array.quiz_total +=answer3
print("\n")

answer4 =  questions["q4"] [input (questions["q4"] ["ques_4"]) ]

quiz_array.quiz_total +=answer4
print("\n")

answer5 =  questions["q5"] [input (questions["q5"] ["ques_5"]) ]

quiz_array.quiz_total +=answer5
print("\n")

answer6 =  questions["q6"] [input (questions["q6"] ["ques_6"]) ]

quiz_array.quiz_total +=answer6
print("\n")

answer7 =  questions["q7"] [input (questions["q7"] ["ques_7"]) ]

quiz_array.quiz_total +=answer7
print("\n")

answer8 =  questions["q8"] [input (questions["q8"] ["ques_8"]) ]

quiz_array.quiz_total +=answer8
print("\n")

answer9 =  questions["q9"] [input (questions["q9"] ["ques_9"]) ]

quiz_array.quiz_total +=answer9
print("\n")

answer10 =  questions["q10"] [input (questions["q10"] ["ques_10"]) ]

quiz_array.quiz_total +=answer10
print("\n")





quiz_functions.final_display (quiz_array.quiz_total)


