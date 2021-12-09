# importing the question dictionary from the questions library
from components.quiz_dictionary import questions
from components import quiz_array, quiz_functions

print ("WELCOME TO WINNIE THE POOH 'guess who' GAME")
print ("Rules: answer the questions asked, and we will guess the character in your mind....Simple rt?! ")
print( "Lets get started...")

answer1 =  questions["q1"] [input (questions["q1"] ["ques_1"]) ]

quiz_array.quiz_total +=answer1

answer2 =  questions["q2"] [input (questions["q2"] ["ques_2"]) ]

quiz_array.quiz_total +=answer2

answer3 =  questions["q3"] [input (questions["q3"] ["ques_3"]) ]

quiz_array.quiz_total +=answer3

answer4 =  questions["q4"] [input (questions["q4"] ["ques_4"]) ]

quiz_array.quiz_total +=answer4

answer5 =  questions["q5"] [input (questions["q5"] ["ques_5"]) ]

quiz_array.quiz_total +=answer5

answer6 =  questions["q6"] [input (questions["q6"] ["ques_6"]) ]

quiz_array.quiz_total +=answer6

answer7 =  questions["q7"] [input (questions["q7"] ["ques_7"]) ]

quiz_array.quiz_total +=answer7

answer8 =  questions["q8"] [input (questions["q8"] ["ques_8"]) ]

quiz_array.quiz_total +=answer8

answer9 =  questions["q9"] [input (questions["q9"] ["ques_9"]) ]

quiz_array.quiz_total +=answer9

answer10 =  questions["q10"] [input (questions["q10"] ["ques_10"]) ]

quiz_array.quiz_total +=answer10





quiz_functions.final_display (quiz_array.quiz_total)


