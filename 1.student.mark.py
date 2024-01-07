# Function to input a number of units (courses / students)
def input_something(args):
    return int(input(f"Enter the number of {args} in this class: "))

# Function to input information for a type (student/course info)
def input_infos(args):
    item = {}
    item['id'] = input("Enter ID: ")
    item['name'] = input("Enter Name: ")
    item['DoB'] = input("Enter Date of Birth (DoB): ")
    return item