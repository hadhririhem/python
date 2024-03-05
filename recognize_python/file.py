num1 = 42  #variable declaration
num2 = 2.3  #variable declaration 
boolean = True   
string = 'Hello World'   #variable declaration string type
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list initialize  
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #tuple initialize 
fruit = ('blueberry', 'strawberry', 'banana') 
print(type(fruit))  # printing what type the fruit data is 
print(pizza_toppings[1]) # access to the second value of the list    
pizza_toppings.append('Mushrooms') # adding the value mushrooms to the list 
print(person['name']) # printing the value associated to name
person['name'] = 'George' # changing the value of name to george 
person['eye_color'] = 'blue' #adding a value 
print(fruit[2]) #access to the third value 

if num1 > 45:                   # if conditional
    print("It's greater")
else:                           # else conditional
    print("It's lower")

if len(string) < 5:              #if conditional
    print("It's a short word!")
elif len(string) > 15:            #elif conditional 
    print("It's a long word!")
else:                              #else conditional
    print("Just right!")

for x in range(5):                #for loop 
    print(x)
for x in range(2,5):           # for loop range(start,stop)
    print(x)
for x in range(2,10,3):        # for loop range(start, stop, sequence)
    print(x)
x = 0                 
while(x < 5):          #while loop
    print(x)         
    x += 1            # increment 

pizza_toppings.pop()  #removing the last value in the list 
pizza_toppings.pop(1)  # removing the second value 

print(person) 
person.pop('eye_color')   #removing the value 
print(person) #print after the changes

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni':  #if conditional
        continue 
    print('After 1st if statement')
    if topping == 'Olives':
        break    #break the loop

def print_hello_ten_times(): #new function 
    for num in range(10):  # for loop range(stop)
        print('Hello')

print_hello_ten_times() #calling the function 

def print_hello_x_times(x): #function with variable
    for num in range(x):
        print('Hello')

print_hello_x_times(4)  #calling the function

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) #  NameError ; variable name is not defined
# num3 = 72  # variable declaration 
# fruit[0] = 'cranberry' #
# print(person['favorite_team'])
# print(pizza_toppings[7]) #Index Error
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1) 