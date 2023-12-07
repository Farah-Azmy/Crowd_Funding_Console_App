# _______functions for project-------
import time
from datetime import datetime

def generate_id():
    id = time.time()
    return round(id)
"""def generate_id_creator():
    id_creator = time.time()
    return round(id_creator)"""

def project_title(message):
  while True:
    title = input(message)
    if title.isalpha():
        return title.lower()
    else:
        print("Enter a valid title ")
  return project_title


def project_details(message):
 while True :
    details = input(message)
    if details.isalpha():
        return details.lower()
    else:
        print("enter valid details")
 return project_details

def target(message):
 while True:
    total_target = input(message)
    if total_target.isdigit():
        return total_target
    else:
        print("enter valid total target")

 return target

def start_date(message):
    while True:
        end_date_str = input(message)
        try:
            star_date = datetime.strptime(end_date_str.strip(), "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Please use MM/DD/YYYY format.")

    # Convert datetime to string before returning
    return star_date.isoformat()


"""def end_date(message):
    while True:
        end_date_str = input(message)
        try:
            end_date = datetime.strptime(end_date_str.strip(), "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Please use MM/DD/YYYY format.")

    return end_date"""
def end_date(message):
    while True:
        end_date_str = input(message)
        try:
            end_date = datetime.strptime(end_date_str.strip(), "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Please use MM/DD/YYYY format.")


    return end_date.isoformat()

#funs ti get project data

project_data_dict = {}
def project_user():

   # creator_id = generate_id_creator(),
    id_project = generate_id()
    project_name = project_title("Enter Project name: ")
    project_info = project_details("Enter project details: ")
    project_target = target("Enter target: ")
    start = start_date("Enter start date (MM/DD/YYYY): ")
    end = end_date("Enter end date (MM/DD/YYYY): ")

    global project_data_dict
    project_data_dict = {
        #(مالهاش لازمه)"id_creator": creator_id,
        "id_project": id_project,
        "project_name": project_name,
        "project_Details": project_info,
        "project_target": project_target,
        "Start_Date": start,
        "End_Date": end,
    }
    """print(project_data_dict)

project_user()"""