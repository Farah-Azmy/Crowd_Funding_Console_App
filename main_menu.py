#for funs that handle other funs
from Handler_file import save_user_data,get_all_data,save_project_data,get_all_projects
from Module_file import get_Password,get_valid_Email,get_valid_lname,get_valid_fname,Mobile_phone,Confirm_password,generate_id,Register_user
from Module_project import project_details,project_title,target,start_date,end_date
import json
import uuid

#get user data
user_data_dict = " "

def Register_user():
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
    #print(user_data_dict)
    save_user_data(user_data_dict)
    return user_data_dict

#get project data
creator_id = ""
project_data_dict = {}
def project_user():
    global creator_id
    creator_id = logged_in_user
    id_project = generate_id()
    project_name = project_title("Enter Project name: ")
    project_info = project_details("Enter project details: ")
    project_target = target("Enter target: ")
    start = start_date("Enter start date (MM/DD/YYYY): ")
    end = end_date("Enter end date (MM/DD/YYYY): ")

    global project_data_dict
    project_data_dict = {
        "id_creator":creator_id,
        "id_project": id_project,
        "project_name": project_name,
        "project_Details": project_info,
        "project_target": project_target,
        "Start_Date": start,
        "End_Date": end,
    }
    #print(project_data_dict)
    save_project_data(project_data_dict)
    return project_data_dict

"""project_user()"""
#funs for login
def login():
    while True:
        email = get_valid_Email("Enter your email: ")
        password = get_Password("Enter your password: ")
        users = get_all_data()

        for user in users:
            if user['Email'] == email and user['password'] == password:
                print("Login successful!")
                print("---------------------")
                return user['id']

        print("Login failed. User not found.")
        return None

logged_in_user = ""
def menu():
    print("Hello in my project")
    print("--------------------------")
    print("Select an option:")
    print("1. Sign Up")
    print("2. Log In")
    print("3. Exit")

    num = input("Enter the number: ")
    if num == "1":
        sign_up = Register_user()
        print(sign_up)
    elif num == "2":
         global logged_in_user
         logged_in_user = login()
         if logged_in_user is not None :
             menu1()

    elif num == "3":
         print("Exiting the menu. Goodbye!")
         exit()
    else:
          print("Invalid option. Please enter a valid number.")


def edit_project():
    projects = get_all_projects()

    for index, pro in enumerate(projects):
        # if 'id_creator' in pro and pro['id_creator'] != int(logged_in_user):
        #     print("You haven't created any projects.")
        #     return None
        if 'id_creator' in pro and pro['id_creator'] == int(logged_in_user):
            print(f"Editing project {index + 1}: {pro}")
            print("------------------------------------------")
    update_id = input("Enter (id_project) which you need to update: ")
    for i, x in enumerate(projects):
        """print(str(update_id )== str(x['id_project']))
        print(update_id, x['id_project'])"""
        if str(update_id )== str(x['id_project']):
            update_field = input("Enter the field to update (e.g., project_name, project_Details, project_target, Start_Date, End_Date): ")
            for i, project in enumerate(projects):
                if 'id_creator' in project and update_id == str(project['id_project']):
                    if update_field in project:
                        new_value = input(f"Enter the new value for {update_field}: ")
                        project[update_field] = new_value
                        print(project)
                        try:
                            filename = 'Project_User.json'
                            with open(filename, 'w') as file:
                                json.dump(projects, file, indent=2)

                            print(f"Project data saved to {filename} successfully.")
                            return project
                        except Exception as e:
                            print(f"Error saving project data: {e}")
                            return None
                    else:
                        print("Invalid field name. Please enter a valid field name.")
                        print("-----------------")
def delete_project():
    projects = get_all_projects()
    for index, pro in enumerate(projects):
        if 'id_creator' in pro and pro['id_creator'] == int(logged_in_user):
            print(f"Deleting project {index + 1}: {pro}")
            enter_id = input("Enter the (id_project) to Delete Project: ")
            for index, project in enumerate(projects):
                if 'id_creator' in project and enter_id == str(project['id_project']):
                  projects.remove(project)
                  try:
                    filename = 'Project_User.json'
                    with open(filename, 'w') as file:
                        json.dump(projects, file, indent=2)

                        print(f"Project data deleted to {filename} successfully.")
                        return project
                  except Exception as e:
                    print(f"Error saving project data: {e}")
                    return None
def menu1():
    print("Welcome back!")
    print("--------------------------")
    print("Select an option:")
    print("1. View projects")
    print("2. Create projects")
    print("3. Edit your project")
    print("4. Delete your project")
    print("5. Log out")

    num = input("Enter the number: ")
    if num == "1":
        view = get_all_projects()
        print(view)
    elif num == "2":
        new_project = project_user()
        print(new_project)
    elif num == "3":
        edit_pro = edit_project()
        print (edit_pro)
    elif num == "4":
        delete_pro = delete_project()
        print(delete_pro)
    elif num == "5":
        print("Exiting the menu. Goodbye!")
        exit()

    else:
        print("Invalid option. Please enter a valid number.")




menu()



