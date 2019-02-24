#Bài tập 1:

# x = int(input("Nhap x: "))
# y = int(input("Nhap y: "))

# k = x + y

# print("Tổng x và y là: ", k )

#Bài tập 2: 
def evaluate(x,y,pt):

    kq = None #result 

    if pt == "+":
        kq = x + y 
    
    elif pt == "-":
        kq = x - y
    
    elif pt == "*":
        kq = x * y
    
    elif pt == "/":
        kq = x / y
        
    else:
        print("Vui lòng chọn đúng phép toán và thử lại: (+) (-) (*) (/) ")
    return kq

# x = int(input("Nhap x: "))
# y = int(input("Nhap y: "))
# pt = str(input("Chon Phep tinh: (+) (-) (*) (/) "))

# r = evaluate(x,y,pt)

# print(r)
    