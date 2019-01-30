#có thay đổi phần in ra 1 xíu =))
a = int(input("Chiều cao của bạn: "))
b = int(input("Cân nặng của bạn: "))
c = a/100
BMI = b/(c*c)
if BMI < 16:
    print("Suy dinh dưỡng à!!!")
elif BMI < 18.5:
    print("Thiếu cân òy!")    
elif BMI < 25:
    print("Ổn đó =))")  
elif BMI < 30:
    print("Thừa cân òy =(")  
else:
    print("Đồ con heo :)")        