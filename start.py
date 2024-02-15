import datetime
# this function is used to create a user account.

def create_account():
    FIRST_NAME = input('Enter your First Name: ')
# while not used for this purpose  when the specific condition doest not meet the  code could not execute.   
# .is alpha only accept alphabet. 
    while not FIRST_NAME.isalpha():
        print("Invalid input! First name should contain only alphabets.")
        FIRST_NAME = input('Enter correct First Name: ')

    LAST_NAME = input('Enter your Last Name: ')
    while not LAST_NAME.isalpha():
        print("Invalid input! Last name should contain only alphabets.")
        LAST_NAME = input('Enter correct Last Name: ')

# .is digit only accept number.
    MOBILE_NUMBER = input('Enter your Mobile Number: ')
    while not (MOBILE_NUMBER.isdigit() and MOBILE_NUMBER[0] == '0' and MOBILE_NUMBER[1] == '3' and len(MOBILE_NUMBER) == 11):
        print("Invalid input! Mobile number should start with 03 and have 11 digits.")
        MOBILE_NUMBER = input('Enter correct Mobile Number: ')

# in this input no specific condition applied.
    ADDRESS = input('Enter your Address: ')
    while not len(ADDRESS) > 3:
        print('Enter some characters for the address.')
        ADDRESS = input('Enter correct Address: ')

    USER_NAME = input('Enter User Name: ')
    while not len(USER_NAME) > 4:
        print('Add more characters .')
        USER_NAME = input('Enter User Name: ')
        

    PASSWORD = input('Enter Password (should be at least 6 characters): ')
    while not  len(PASSWORD) >=6:
        print("Invalid input! Password should be at least 6 characters.")
        PASSWORD = input('Enter Password: ')
# I have opened the file in read mode with the append1-plus (+) option.
#  If an account exists, it should be read; otherwise, it should not throw an error. Additionally, since there is no f.write, nothing will be written to the file due to this reason."
    with open('user_info.txt', 'a+') as file:
# iterate line by line.
        for line in file:
# strip remove space and split convert each informatin in to string and the process of slicing will be done.
            stored_user_info = line.strip().split(',')
# when new user_name or password match with existing user_name this code provide  some restriction.
            stored_username, stored_password = stored_user_info[-2], stored_user_info[-1]
# 
            if stored_username == USER_NAME:
                print('This username is already taken. Please choose another one.')
                create_account()
                return
                
            elif stored_password == PASSWORD:
                print('This password is already in use. Please choose another one.')
                create_account()
                return
    

        

    # Combine user information into a list
    user_info = [FIRST_NAME, LAST_NAME, MOBILE_NUMBER, ADDRESS, USER_NAME, PASSWORD]

    # Save user information to a file
    with open('user_info.txt', 'a') as file:
        file.write(','.join(user_info) + '\n')
    print('Account created successfully!')
# return user_name beacuse it will be user in filing history of user.
    return  USER_NAME

def sign_in():
    username_to_find = input("Enter your username for sign-in: ")
    password_to_find = input("Enter your password for sign-in: ")

    # Read user information from the file and check for a match
    with open('user_info.txt','a+') as file:
# seek used the checking start from the start.
        file.seek(0)
        for line in file:
            stored_user_info = line.strip().split(',')
            #print(stored_user_info,'chck')
            stored_username, stored_password = stored_user_info[-2], stored_user_info[-1]

            if stored_username == username_to_find and stored_password == password_to_find:
                print("Sign-in successful!")
#return user_name because it will be used to name the file of user_history.              
                return username_to_find
            
        else:
            print("Invalid username or password. Sign-in failed.")
# again call.
            sign_in()
#  This function displays the initial welcome message and takes user's choice.
def welcome_message():
    print("WELCOME TO FOODI RESTAURANT!")
    print("1. Create an Account")
    print("2. Sign In")

welcome_message()
# THIS IS THE MAIN FUNCTION TO START THE PROGRAM.
            
# GLOBAL THE USER SO IT WILL BE USED IN FUNCTIONS.
def start():
            global user
            choice = input('Enter your choice: ')

            if choice == '1':
                user=create_account()
# STOR USER_NAME IN USER VARIABLE.       
                return

            elif choice == '2':
                user=sign_in()
                
                return

            else:
                print('Invalid choice. Please enter 1 or 2.')
                start()    
# product_dict contain a dictionary .
product_dict = {
    1: ['PIZZA  ', '1200'],
    2: ['BURGER ', '300'],
    3: ['CAKE   ', '200'],
    4: ['PASTA  ', '100'],
    5: ['BIRYANI', '300'],
    6: ['VEGROLL', '250'],
    7: ['SALAD  ', '350'],
    8: ['TIKKA  ', '600'],
    9: ['NOODLES', '800'],
    10:['COFEE ', '1000']
}
with open ('product_dict.txt','a')as file:
    file.write(str(product_dict))
# no restriction how much you want beacuse its resturant no restriction for quantity.

start()

def display_menu(product_dict):
    print("Menu:")
    # PRODUCT ID have SERIAL NUMBERS ,PRODUCT NAME have SIMPLE PRODUCT NAME  AND THE LOOP ITERATE.
    for product_NO, details in product_dict.items():
        product_name = details[0]
        price = details[1]
        print(f"{product_NO}. {product_name}, Price: {price}")

# CART INTIALIZE AS A GLOBAL.
cart = []

def add_to_cart(product_list, cart):
# WHILE LOOP ADD PRODUCT IN TO CART AS MUCH AS YOU CAN.
    while True:
        user_input = input('Enter product number which one you want\n (enter 0 when you are finish):')
# ONLY DIGIT CAN BE ENTER.
        if user_input.isdigit():
            user_input = int(user_input)
# CONVERT IN TO INTEGER TO FUTHER USE EASILY IN OTHER CONDITION.
            if 0 < user_input < 11:

# new variable list which have lists of product_dict .
                list = product_list[user_input]
                product = list[0]
                price = list[1]
 # this loop for quantity.
                while True: 
                   Quantity = input(f'Enter quantity for {product}: ')
                   if Quantity.isdigit() and int(Quantity) > 0:
                        Quantity = int(Quantity)
                        price=int(price)*(int(Quantity))
# all information of product append in to cart.
                        cart.append([product_list[user_input][0], Quantity ,price])
                        break
                   else:
                        print('Invalid quantity. Please enter a positive integer.')

            elif user_input == 0:
                print('You have finished adding products to the cart.')
#this elif will be break when our work in done.
                break
            else:
                print('Invalid product number. Please enter a number between 1 and 10.')
# thise else execute when the enter chractor is not digit.
        else:
            print('Invalid input. Please enter a valid number.')
    return cart

def user_history(cart):
# take the information from cartwhich user enter in add_to_cart.
    for i in range(len(cart)):
        print(i + 1, '.', 'Quantity', cart[i][1], 'product', cart[i][0], 'Rs', cart[i][2])
        # list have sublist  for each product and the loop iterate in sublist.
    return cart
# user_history(cart)

def user_remove_history(cart):
    while True:
        print('You want to remove items')
        remove_input = input('Enter the number of the item you want to remove (enter 0 to finish): ')

        if remove_input.isdigit():
            remove_input = int(remove_input)

            if 0 < remove_input <= len(cart):
# pop use to delete the item and return the removed item.
                removed_item = cart.pop(remove_input - 1)
                
# it gives user item information .
                print(f'Removed: Quantity {removed_item[1]}, Product {removed_item[0]}, Rs. {removed_item[2]}')
            elif remove_input == 0:
                print('You have finished removing items.')
# the work has been donne at this point.
                break
            else:
                print('Invalid input. Please enter a number between 1 and', len(cart))
        else:
            print('Invalid input. Please enter a valid number.')

    return cart

# check out calculate total price.
def check_out(cart):
    total_price = 0
# total calculate ho raha ha   
    for i in range(len(cart)):
# addition of two or more product prises done here.
        price=cart[i][2]
        total_price =total_price+price
# store user_history with date, time ,month. 
        date=datetime.datetime.now()
        date=date.strftime('%Y-%m-%d%H:%M:%S')
#  return price .   
    return total_price

def welcome():
    print("WELCOME TO FOODI RESTAURANT!")
    print("1. Display Menu and Add to Cart")
    print("2. View Cart and Remove Items")
    print("3. View Cart Total (check_out):")

while True:
    welcome()

    choice = input('Enter number which side you want to visit:')

    if choice == '1':
        display_menu(product_dict)
        add_to_cart(product_dict, cart)
    elif choice == '2':
        user_history(cart)
        user_remove_history(cart)
    elif choice == '3':
        total_price = check_out(cart)
        print(f'Your total bill is Rs. {total_price}')
        print('THANKS FOR VISITNG OUR APP')
# APPEND MODE on and the file of  each user_name will be created and this file have user_history.
        with open(user+'.txt','a+') as file:
            date=datetime.datetime.now()
            date=date.strftime('%Y-%m-%d%H:%M:%S')
            D={}
            D[date]=cart
            file.write(str(D)+'\n')
            break
    else:
        print('Invalid choice. Please enter a number between 1 and 3.')
        
        
