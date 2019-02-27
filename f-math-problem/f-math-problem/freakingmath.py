from random import *
from random import randint, choice

def generate_quiz():
    x = randint(0,9)
    y = randint(0,9)
    op = "+"
    result = x + y  + randint(-1,1)
    # Hint: Return [x, y, op, result]
    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    # print(result)
    if x + y == result:
        if user_choice == True:
            return True
        else:
            return False
        
    else:
        if user_choice == False:
            return True
        else:
            return False
       
    
