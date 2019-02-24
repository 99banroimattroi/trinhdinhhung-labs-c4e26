from random import randint, choice
import calc
x = randint(0,9)
y = randint(0,9)
pt = choice(["+","-","*","/"])
error = randint(-1,1)
r = calc.evaluate(x,y,pt) + error


# string formating
s = f"{x} {pt} {y} = {r}"
print("*"*50)
print(s)
print("*"*50)


# print("%d + %d = %d"%(x,y,z))


user_answer = input("(Y)es or (N)o ? ")

if error == 0:
    if user_answer == "y":
        print("Yay")
    else:
        print("Oh no !")
else:
    if user_answer == "y":
        print("Yay")
    else:
        print("Oh no !")






