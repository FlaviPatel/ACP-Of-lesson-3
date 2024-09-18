x = int(input("Enter the total number of working days:"))
y = int(input("Enter the total number of absent days:"))

percentage = (x - y )/ x * 100

print('Percentage', percentage)

if percentage <= 75:
         print("You are not eligible for sitting in exam")

else:
    print("You are eligible for exam")