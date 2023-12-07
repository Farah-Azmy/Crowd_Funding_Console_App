from Module_file import Register_user as r
from Module_project import project_user
import json

def save_user_data(user_data_dict : dict):
    old_data = get_all_data()
    old_data.append(user_data_dict)
    valid_data = json.dumps(old_data, indent=2)
    try:
        fileobj = open("User_data.json", "w")
    except Exception as e:
             return  False
    else:

        fileobj.write(valid_data)
        fileobj.close()
        return True


def get_all_data():
    try:
        filobject = open("User_data.json","r")
    except Exception as e:
        print(e)
    else:
        data = filobject.read()
        filobject.close()
        data = data.strip('\n')
        if data:
            file_data = json.loads(data)
            return file_data
        return []

#create project json
def save_project_data(project_data_dict : dict):
    data_pro = get_all_projects()
    data_pro.append(project_data_dict)
    valid_data = json.dumps(data_pro, indent=2)
    try:
        fileobj = open("Project_User.json", "w")
    except Exception as e:
             return  False
    else:

        fileobj.write(valid_data)
        fileobj.close()
        return  True


def get_all_projects():
    try:
        filobject = open("Project_User.json","r")
    except Exception as e:
        print(e)
    else:
        data = filobject.read()
        filobject.close()
        data = data.strip('\n')
        if data:
            file_data = json.loads(data)
            return  file_data
        return []




import json

"""def edit_project_data(project):

    filename = 'project_Data.json'

    try:
        with open(filename, 'w') as file:
            json.dump(projects, file, indent=2)
        print(f"Project data saved to {filename} successfully.")
    except Exception as e:
        print(f"Error saving project data: {e}")
"""


