# This is my Project
# Python To Do List

def adding():
    # ask user to enter subject and time
    print("To Do:")
    subject = str(input())
    print('Time (a number between 0 and 24):')
    hour = input()

    # if user input is a number, convert to int
    if hour.isdigit():
        hour = int(hour)

    elif not hour.isdigit():
        print("Try again, with a number between 0 - 24")

    if hour < 0 or hour > 24:
        print("Try again, with a number between 0 - 24")

    elif hour > 0 and hour < 24:
        if hour in todo_list:
            print("This slot is taken with", todo_list[hour], "do you want to overwrite? yes/no")
            overwrite = str(input())
            if overwrite == "yes":
                print("Are you sure?")
                sure = str(input())
                if sure == "yes":
                    todo_list[hour] = subject
                    print("At", str(hour), "you are now doing", subject)
                else:
                    print("nothing changed")

        elif hour not in todo_list:
            todo_list[hour] = subject
            print("At", str(hour), "you are now doing", subject)

def delete():
    print("Which appointment do you want to delete? Please Enter the time (0-24)")
    delete = input()

    if delete.isdigit():
        delete = int(delete)

    elif not delete.isdigit():
        print("Try again, with a number between 0 - 24")

    if delete < 0 or delete > 24:
        print("Try again, with a number between 0 - 24")

    elif delete > 0 and delete < 24:
        if delete in todo_list:
            todo_list.pop(delete)
            hours = todo_list.keys()
            hours_sorted = sorted(hours)
            for i in hours_sorted:
                print("Remaining:\n", "Hour:", i, "Appointment:", todo_list[i])

        elif delete not in todo_list:
            print("You don't have an appointment at", str(delete))

def check():
    hours = todo_list.keys()
    hours_sorted = sorted(hours)

    for i in hours_sorted:
        print("Hour:", i, "Appointment:", todo_list[i])

todo_list = {}

check()
if len(todo_list) == 0:
    print("Your List is empty.")

print("Do you want to add or delete an appointment?")
answer = input("to add type add / to delete type delete\n")

if answer == "add":
    adding()

elif answer == "delete":
    delete()

else:
    print('Try again, with "add" or "delete" ')

print("Do you want to add / delete / check")
anything_else = input()


while anything_else == "add":
    adding()
    anything_else = input("anything else? add / delete / check\n")

while anything_else == "delete":
    delete()
    anything_else = input("anything else? add / delete / check\n")

while anything_else == "check":
    check()
    anything_else = input("anything else? add / delete / check\n")

else:
    print("Goodbye")