
import re
import time

def generate_id():
    id = time.time()
    return round(id)

def get_valid_fname(message):
    while True:
        f_name = input(message)
        if f_name.isalpha():
            return f_name.lower()
        else:
            print("Enter a valid name.")

def get_valid_lname(message):
    while True:
        l_name = input(message)
        if l_name.isalpha():
            return l_name.lower()
        else:
            print("Enter a valid name.")

def get_valid_Email(message):
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    while True:
        email = input(message)
        if re.match(email_pattern, email):
            return email
        else:
            print(" Please enter a valid email address.")

#uses nonlocal
def password_functions():

    password = ""
    def get_Password(message):
        nonlocal password
        password = input(message)
        return password

    def Confirm_password(message):
        nonlocal password
        while True:
            confirm_password = input(message)
            if password == confirm_password:
                    return password
            else:
                  print("Password and confirm password do not match. Please try again.")
    return get_Password, Confirm_password
#unpack functions
get_Password, Confirm_password = password_functions()

def Mobile_phone(message):
    phone_pattern = re.compile(r'^\+(20)(1|2|5)\d{9}$')
    while True:
        mobile_phone = input(message)
        if re.match(phone_pattern, mobile_phone):
            return mobile_phone
        else:
            print("Invalid mobile phone number. Please enter a valid Egyptian phone number.")

# funs to get user data
user_data_dict = {}
def Register_user():
    #user = read_file()
    id = generate_id()
    first_name = get_valid_fname("Enter your first name: ")
    last_name = get_valid_lname("Enter your last name: ")
    email_user = get_valid_Email("Enter your email: ")
    mobile_phone = Mobile_phone("Enter your mobile phone number (Egyptian): ")
    password_user = get_Password("Enter password: ")
    confirm_password = Confirm_password("Confirm password:")
    global user_data_dict
    user_data_dict = {
        "id": id,
        "First_name": first_name,
        "Last_name": last_name,
        "Email": email_user,
        "mobile": mobile_phone,
        "password": password_user,
        "confirm_password": confirm_password
    }
    print(user_data_dict)




