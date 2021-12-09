#pass the quiz total over here....import array over here....check the value and and print out the names and the corresponding images.

from components import quiz_array

def final_display (total):
    
    #pooh        7000-8000   
    if total > 6000 and total<=7000:
        print(quiz_array.characters[0])

    #robin         0-100
    if total >= 0 and total<=100:
        print(quiz_array.characters[1])

    #kanga
    if  total >= 20000:
        print(quiz_array.characters[2])

     #trigger   100 - 1000 
    if  total > 100 and total<=1000:
        print(quiz_array.characters[3])                


    #rabbit  1000-2000
    if total > 1000 and total<=2000:
        print(quiz_array.characters[4])

     #pigglet   2000-3000
    if  total > 2000 and total<=3000:
        print(quiz_array.characters[5])

     #eeyore   3000-4000 
    if  total > 3000 and total<=4000:
        print(quiz_array.characters[6])

     #roo    4000-5000
    if total > 4000 and total<=5000:
        print(quiz_array.characters[7])

    #owl 
    if total > 4000 and total<=5000:
        print(quiz_array.characters[8])    

                      

  






      