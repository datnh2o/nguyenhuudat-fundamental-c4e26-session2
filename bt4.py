#ý a
for i in range(19):
    print("*", end=" ") 
print(" ")
#ý b
b = int(input("Enter a number: "))
for i in range(1, b+1):
    print("*", end=" ")
print(" ")
#ý c
for i in range(9):
    if i%2==0:
        print("x", end=" ")
    else:
        print("*", end=" ")             
print(" ")
#ý d
d = int(input("Enter a number: "))
for i in range(0, d):
    if i%2==0:
        print("x", end=" ")
    else:
        print("*", end=" ")       
print()
#ý f
for i in range(21):
    print("*", end=" ")
    if i%7==6:
        print("") 
print()
#ý g
n = int(input("Nhập số cột: "))
m = int(input("Nhập số hàng: "))
for i in range(m*n):
    print("*", end=" ")
    if i%n==(n-1):
        print("")         
          