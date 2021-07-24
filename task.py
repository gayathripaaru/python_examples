print('Available Toppings are: \n Onions \n Lettuce \n Tomato \n Olives \n Peppers \n Tomatoes')

Toppings =[x for x in input('Enter any three Toppings seperated by space: ').split()]

print(Toppings)

count=int(input("How many Toppings: "))

print(count)

print("Total in $: ", 5*count)

