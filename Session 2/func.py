def say_hello(name):   #function parameters
    print("hello C4E26", name)
    print("Have a nice day")
    print("bye bye")
#call function
say_hello("Trinh")  #Trinh
say_hello("Dinh")   #Dinh
say_hello("Hung")   #Hung

#Bài tập:
def add(a,b):  #scpoe
    s = a+b
    print(s)
    return s # cho phép lưu s sử dụng nằm ngoài hàm
t = add(3,4)

print(t)