#pass the quiz total over here....import array over here....check the value and and print out the names and the corresponding images.
from PIL import Image
from components import quiz_array


def final_display (total):
    
    #pooh        7000-8000   
    if total > 7000 and total<=8000:
        print(quiz_array.characters[0])
        pooh = Image.open("images/pooh.jpg")
        pooh.show()


    #robin         0-100
    if total >= 0 and total<=100:
        print(quiz_array.characters[1])
        robin = Image.open("images/robin.jpg")
        robin.show()

    #kanga
    if  total >= 20000:
        print(quiz_array.characters[2])
        kanga = Image.open("images/kanga.jpg")
        kanga.show()

     #trigger   100 - 1000 
    if  total > 100 and total<=1000:
        print(quiz_array.characters[3])  
        trigger = Image.open("images/trigger.jpg")
        trigger.show()              


    #rabbit  1000-2000
    if total > 1000 and total<=2000:
        print(quiz_array.characters[4])
        rabbit = Image.open("images/rabbit.jpg")
        rabbit.show()

     #pigglet   2000-3000
    if  total > 2000 and total<=3000:
        print(quiz_array.characters[5])
        pigglet = Image.open("images/pigglet.jpg")
        pigglet.show()

     #eeyore   3000-4000 
    if  total > 3000 and total<=4000:
        print(quiz_array.characters[6])
        eeyore = Image.open("images/Eeyore.jpg")
        eeyore.show()

     #roo    4000-5000
    if total > 4000 and total<=5000:
        print(quiz_array.characters[7])
        roo = Image.open("images/roo.jpg")
        roo.show()

    #owl 
    if total > 4000 and total<=5000:
        print(quiz_array.characters[8])  
        owl = Image.open("images/owl.jpg")
        owl.show()  

                      

  






      