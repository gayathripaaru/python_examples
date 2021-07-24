user = input('How far would like to travel in miles?')
user = int (user)
if user < 3:
    print("walk")
elif user < 300:
    print("drive")
else:
    print("fly")
