n = int(input("Enter a number: "))
for i in range(1, n):
    print(i, end=" ")
print(" ")
m = int(input("Enter a number: "))
for i in range(0, m+1, 2):
    print(i, end=" ")
print(" ")
k = int(input("Enter a number: "))
s = 0
for i in range(k + 1):
    s += i
print(s)
print(sum(range(1, k+1)))