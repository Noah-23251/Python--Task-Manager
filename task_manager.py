# Thanks for the feedback
# That was awful, I had to rewrite the whole section to fix it, and I noticed some errors in the calculations too, while
# I was sorting it out! I think it's fine now, I couldn't spot any other issues anyway.
# Thanks for checking, and fingers crossed!

# ====importing libraries====
# I found this method of importing the date at https://www.geeksforgeeks.org/get-current-date-using-python/
from datetime import datetime
current_date_time = datetime.today()
date_time_list = (str(current_date_time)).split(" ")
current_date = date_time_list[0]


# ====Defining functions====
def reg_user(new_user, new_pass):
    with open("user.txt", "r+") as user_text:
        if new_user not in user_text:
            user_text.write("\n" + new_user + ", " + new_pass)
        else:
            print("User already exists")


def add_task(task_number, task_user, task_title, task_description, task_deadline, task_completion):
    with open("tasks.txt", "a") as tasks_text:
        tasks_text.write("\n" + task_number + ", " + task_user + ", " + task_title + ", " + task_description + ", " +
                         task_deadline + ", " + str(current_date) + ", " + task_completion)


def view_all():
    with open("tasks.txt", "r") as tasks_text:
        for a in tasks_text:
            list_1 = (a.strip("\n")).split(", ")
            print(f"""
Task number:            {list_1[0]}
Task:                   {list_1[2]}  
Assigned to:            {list_1[1]} 
Date assigned:          {list_1[5]}
Due date:               {list_1[4]} 
Task Complete?          {list_1[6]} 
Task description:
 {list_1[3]}
                    """)


def view_mine(user_name):
    with open("tasks.txt", "r") as tasks_text:
        for a in tasks_text:
            list_1 = (a.strip("\n")).split(", ")
            if user_name == list_1[1]:
                print(f"""
    Task number:            {list_1[0]}
    Task:                   {list_1[2]}  
    Assigned to:            {list_1[1]} 
    Date assigned:          {list_1[5]}
    Due date:               {list_1[4]} 
    Task Complete?          {list_1[6]} 
    Task description:
     {list_1[3]}
                        """)


# Creating list of task numbers
task_numbers_list = []
with open("tasks.txt", "r") as tasks_text:
    for a in tasks_text:
        list_1 = (a.strip("\n")).split(", ")
        task_numbers_list.append(list_1[0])

# Clearing overview documents
with open("tasks_holding.txt", "w") as f:
    pass
with open("user_overview.txt", "w") as g:
    pass

# ====Login Section====
# Create empty dictionary for login details, and then empty lists for the loop
login_details = {}
users_list = []
usernames_list = []
list_pairs = []

# Use for loop to add users/passwords to the dictionary
with open("user.txt", "r") as users:
    for line in users:
        users_list.append(line.strip("\n"))
    for item in users_list:
        list_pairs = item.split(", ")
        login_details[list_pairs[0]] = list_pairs[1]
        usernames_list.append(list_pairs[0])

# Create empty variables
login_correct = False
user_name = ""
password = ""

# Use loops to request username and password until username is in dictionary and the password given matches the
# dictionary
while not login_correct:
    user_name = (input("Please enter your username ")).lower()
    if user_name in login_details:
        password = input("Please enter your password ")
        if login_details[user_name] != password:
            while login_details[user_name] != password:
                print("Password incorrect")
                password = input("Please enter your password ")
        else:
            login_correct = True
    else:
        print("User not recognised")

while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - View task statistics
e - Exit
: ''').lower()

    if menu == 'r':
        # Only allows the user to proceed if they are logged in as admin
        if user_name == "admin":
            # Request details from user and use loop to confirm password
            new_username = (input("Please enter the new user's name ")).lower()
            new_password = input("Please enter the new user's password ")
            new_password_2 = input("Please confirm the new user's password ")
            if new_password_2 != new_password:
                while new_password_2 != new_password:
                    new_password_2 = input("New passwords do not match, please try again ")
            else:
                # Register new user and print confirmation
                reg_user(new_username, new_password)
                print(f"New user {new_username} added\n")
        else:
            print("Current user does not have the rights to add new users\n")

        pass

    elif menu == 'a':
        # Request details of task from user
        tasks_list = []
        with open("tasks.txt", "r") as tasks_1:
            for line_1 in tasks_1:
                tasks_list.append(line_1)
        task_number = str((len(tasks_list) + 1))
        task_user = input("Please enter the user who the new task is assigned to ")
        task_title = input("Please enter the title of the new task ")
        task_description = input("Please enter the description of the new task ")
        task_deadline = input("Please enter the due date of the new task (yyyy-mm-dd) ")
        task_completion = "No"
        # Write to tasks.txt and print confirmation - method for writing to tasks.txt from previous feedback (thanks!)
        add_task(task_number, task_user, task_title, task_description, task_deadline, task_completion)
        print(f"New task {task_title} added\n")
        pass

    elif menu == 'va':
        # Use view_all function to display all tasks
        view_all()
        pass

    elif menu == 'vm':
        # Use view_mine function to display all users tasks
        view_mine(user_name)
        # Request input for task to be edited. If the task number is in the list and the user hasn't entered -1, then
        # they can proceed to edit tasks
        task_request = input(
            "Please enter the number of the task you wish to edit, or enter -1 to return to the main menu ")
        valid_task = task_request in task_numbers_list
        if not valid_task and task_request != "-1":
            print("Task number invalid, returning to main menu")
            pass
        else:
            if task_request == "-1":
                pass
            else:
                # Create list of values in the line of tasks.txt which is to be edited, and a counter variable to keep
                # track of the line which is being edited
                task_edit_list = []
                counter = 0
                with open("tasks.txt", "r") as original_text:
                    for a in original_text:
                        list_1 = (a.strip("\n")).split(", ")
                        counter += 1
                        if task_request == list_1[0]:
                            for item in list_1:
                                task_edit_list.append(item)
                            break
                # If task to be edited is marked as complete, then return to main menu
                if task_edit_list[6] == "Yes":
                    print("Task is complete, and therefore cannot be edited\n")
                else:
                    # Request changes to tasks and edit the task_edit_list accordingly. Transcribe from tasks.txt into
                    # holding.txt (adding the task_edit_values as appropriate) and then overwrite tasks.txt with the new
                    # values
                    mark_complete = input("Mark task as complete (Yes/No)? ").lower()
                    if mark_complete == "yes":
                        task_edit_list[6] = "Yes"
                        with open("tasks_holding.txt", "w") as holding_text, open("tasks.txt", "r") as original_text:
                            for b in original_text:
                                list_2 = (b.strip("\n")).split(", ")
                                if str(counter) != list_2[0]:
                                    holding_text.write(list_2[0] + ", " + list_2[1] + ", " + list_2[2] + ", " +
                                                       list_2[3] + ", " + list_2[4] + ", " + list_2[5] + ", " +
                                                       list_2[6] + "\n")
                                else:
                                    holding_text.write(task_edit_list[0] + ", " + task_edit_list[1] + ", " +
                                                       task_edit_list[2] + ", " + task_edit_list[3] + ", " +
                                                       task_edit_list[4] + ", " + task_edit_list[5] + ", " +
                                                       task_edit_list[6] + "\n")
                        with open("tasks_holding.txt", "r") as holding_text, open("tasks.txt", "w") as new_text:
                            for line in holding_text:
                                new_text.write(line)
                    task_edit = input("Edit the task (Yes/No)? ").lower()
                    if task_edit == "yes":
                        assignment = input("Change the allocation of the task? ").lower()
                        if assignment == "yes":
                            new_assignment = input("Please enter the name of the user who you wish to allocate the task to ").lower()
                            if new_assignment in users_list:
                                task_edit_list[1] = new_assignment
                                with open("tasks_holding.txt", "w") as holding_text, open("tasks.txt", "r") as original_text:
                                    for c in original_text:
                                        list_3 = (c.strip("\n")).split(", ")
                                        if str(counter) != list_3[0]:
                                            holding_text.write(list_3[0] + ", " + list_3[1] + ", " + list_3[2] + ", " +
                                                               list_3[3] + ", " + list_3[4] + ", " + list_3[5] + ", " +
                                                               list_3[6] + "\n")
                                        else:
                                            holding_text.write(task_edit_list[0] + ", " + task_edit_list[1] + ", " +
                                                               task_edit_list[2] + ", " + task_edit_list[3] + ", " +
                                                               task_edit_list[4] + ", " + task_edit_list[5] + ", " +
                                                               task_edit_list[6] + "\n")
                                with open("tasks_holding.txt", "r") as holding_text, open("tasks.txt", "w") as new_text:
                                    for line in holding_text:
                                        new_text.write(line)
                        else:
                            pass
                        due_date = input("Change the due date of the task? ").lower()
                        if due_date == "yes":
                            new_date = input("Please enter the new due date for the task (yyyy-mm-dd)")
                            task_edit_list[4] = new_date
                            with open("tasks_holding.txt", "w") as holding_text, open("tasks.txt", "r") as original_text:
                                for d in original_text:
                                    list_4 = (d.strip("\n")).split(", ")
                                    if str(counter) != list_4[0]:
                                        holding_text.write(
                                            list_4[0] + ", " + list_4[1] + ", " + list_4[2] + ", " +
                                            list_4[3] + ", " + list_4[4] + ", " + list_4[5] + ", " +
                                            list_4[6] + "\n")
                                    else:
                                        holding_text.write(task_edit_list[0] + ", " + task_edit_list[1] + ", " +
                                                           task_edit_list[2] + ", " +
                                                           task_edit_list[3] + ", " + task_edit_list[4] + ", " +
                                                           task_edit_list[5] + ", " +
                                                           task_edit_list[6] + "\n")
                            with open("tasks_holding.txt", "r") as holding_text, open("tasks.txt", "w") as new_text:
                                for line in holding_text:
                                    new_text.write(line)
                        else:
                            pass
        pass

    elif menu == "gr":
        # Only allows the user to proceed if they are logged in as admin
        if user_name == "admin":
            # Create empty variables
            complete_tasks = 0
            incomplete_tasks = 0
            total_tasks = 0
            task_overdue = 0
            # Loop through tasks.txt and update variables as appropriate
            with open("tasks.txt", "r") as tasks_text:
                for e in tasks_text:
                    list_5 = (e.strip("\n")).split(", ")
                    if list_5[6] == "Yes":
                        complete_tasks += 1
                    else:
                        incomplete_tasks += 1
                    due_date = datetime.strptime(list_5[4], "%Y-%m-%d")
                    if due_date < datetime.strptime(current_date, "%Y-%m-%d"):
                        task_overdue += 1
                    total_tasks += 1
            incomplete_percentage = (incomplete_tasks / total_tasks) * 100
            overdue_percentage = (task_overdue / total_tasks) * 100
            # Write stats to task_overview.txt
            with open("task_overview.txt", "w") as overview:
                overview.write(f"""
Task Overview
Total tasks registered:         {total_tasks}
Total complete tasks:           {complete_tasks}
Total incomplete tasks:         {incomplete_tasks}
Total tasks overdue:            {task_overdue} 
Percentage incomplete:          {incomplete_percentage}%
Percentage overdue:             {overdue_percentage}%    
""")
            # Loop through tasks.txt for each user in users_list, recording relevant data, and then adding this to
            # user_overview.txt
            for user in usernames_list:
                current_user = ""
                user_total = 0
                user_task_percentage = 0
                user_complete_tasks = 0
                user_incomplete_tasks = 0
                user_overdue_tasks = 0
                total_tasks = 0
                user_complete_percentage = 0
                user_incomplete_percentage = 0
                user_overdue_percentage = 0
                with open("tasks.txt", "r") as tasks_text:
                    for e in tasks_text:
                        list_6 = (e.strip("\n")).split(", ")
                        if list_6[1] == user:
                            current_user = list_6[1]
                            user_total += 1
                            if list_6[6] == "Yes":
                                user_complete_tasks += 1
                            else:
                                user_incomplete_tasks += 1
                            due_date = datetime.strptime(list_6[4], "%Y-%m-%d")
                            if due_date < datetime.strptime(current_date, "%Y-%m-%d") and list_6[6] == "No":
                                user_overdue_tasks += 1
                        total_tasks += 1
                if current_user == user:
                    if total_tasks > 0:
                        user_task_percentage = (user_total / total_tasks) * 100
                    else:
                        user_task_percentage = 0
                    if user_total > 0:
                        user_complete_percentage = (user_complete_tasks / user_total) * 100
                        user_incomplete_percentage = (user_incomplete_tasks / user_total) * 100
                    else:
                        user_complete_percentage = 0
                        user_incomplete_percentage = 0
                    if user_incomplete_tasks > 0:
                        user_overdue_percentage = (user_overdue_tasks / user_incomplete_tasks) * 100
                    else:
                        user_overdue_percentage = 0
                    with open("user_overview.txt", "a") as overview:
                        overview.write(f"""
User {user}
Tasks assigned:             {user_total}
Percentage of total tasks:  {user_task_percentage}
Complete tasks:             {user_complete_percentage}%
Incomplete tasks:           {user_incomplete_percentage}%
Overdue tasks:              {user_overdue_percentage}%
""")
                else:
                    pass
            print("Reports generated\n")
        else:
            print("Current user does not have the rights to generate reports\n")

    elif menu == "ds":
        # Opened user_overview.txt with w, just to clear any data in case reports were generated previously
        with open("user_overview.txt", "w") as g:
            pass
        # Create empty variables and generate overview documents (as above)
        complete_tasks = 0
        incomplete_tasks = 0
        total_tasks = 0
        task_overdue = 0
        with open("tasks.txt", "r") as tasks_text:
            for e in tasks_text:
                list_5 = (e.strip("\n")).split(", ")
                if list_5[6] == "Yes":
                    complete_tasks += 1
                else:
                    incomplete_tasks += 1
                due_date = datetime.strptime(list_5[4], "%Y-%m-%d")
                if due_date < datetime.strptime(current_date, "%Y-%m-%d"):
                    task_overdue += 1
                total_tasks += 1
        incomplete_percentage = (incomplete_tasks / total_tasks) * 100
        overdue_percentage = (task_overdue / total_tasks) * 100
        with open("task_overview.txt", "w") as overview:
            overview.write(f"""
Task Overview
Total tasks registered:         {total_tasks}
Total complete tasks:           {complete_tasks}
Total incomplete tasks:         {incomplete_tasks}
Total tasks overdue:            {task_overdue} 
Percentage incomplete:          {incomplete_percentage}%
Percentage overdue:             {overdue_percentage}%    
""")
        for user in usernames_list:
            current_user = ""
            user_total = 0
            user_task_percentage = 0
            user_complete_tasks = 0
            user_incomplete_tasks = 0
            user_overdue_tasks = 0
            total_tasks = 0
            user_complete_percentage = 0
            user_incomplete_percentage = 0
            user_overdue_percentage = 0
            with open("tasks.txt", "r") as tasks_text:
                for e in tasks_text:
                    list_6 = (e.strip("\n")).split(", ")
                    if list_6[1] == user:
                        current_user = list_6[1]
                        user_total += 1
                        if list_6[6] == "Yes":
                            user_complete_tasks += 1
                        else:
                            user_incomplete_tasks += 1
                        due_date = datetime.strptime(list_6[4], "%Y-%m-%d")
                        if due_date < datetime.strptime(current_date, "%Y-%m-%d") and list_6[6] == "No":
                            user_overdue_tasks += 1
                    total_tasks += 1
            if current_user == user:
                if total_tasks > 0:
                    user_task_percentage = (user_total / total_tasks) * 100
                else:
                    user_task_percentage = 0
                if user_total > 0:
                    user_complete_percentage = (user_complete_tasks / user_total) * 100
                    user_incomplete_percentage = (user_incomplete_tasks / user_total) * 100
                else:
                    user_complete_percentage = 0
                    user_incomplete_percentage = 0
                if user_incomplete_tasks > 0:
                    user_overdue_percentage = (user_overdue_tasks / user_incomplete_tasks) * 100
                else:
                    user_overdue_percentage = 0
                with open("user_overview.txt", "a") as overview:
                    overview.write(f"""
User {user}
Tasks assigned:             {user_total}
Percentage of total tasks:  {user_task_percentage}
Complete tasks:             {user_complete_percentage}%
Incomplete tasks:           {user_incomplete_percentage}%
Overdue tasks:              {user_overdue_percentage}%
""")
            else:
                pass
        # Only allows the user to proceed if they are logged in as admin
        if user_name == "admin":
            # Print contents of the overview files in the console
            with open("user_overview.txt", "r") as user_text, open("task_overview.txt", "r") as task_text:
                print(user_text.read())
                print(task_text.read())
        else:
            print("Current user does not have the rights to view statistics\n")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
