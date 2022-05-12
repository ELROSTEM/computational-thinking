from statistics import mean


def pretty_print(list):
    for i in list:
        print(i)


######################################################################################################
"""
Read the data from txt file
"""

# File name
infile = "Employee_2021-22.txt"

# Read the Data into a list with dictionaries
data = []
with open(infile, 'r') as f:
    for line in f:
        # Turns each line into a string
            # First it makes it a raw string
            # Then it replaces \t and \n with spaces
            # Lastly it gets rid of the extra ' in the string
        line = repr(line).replace(r'\t', ' ').replace(r'\n', ' ').lstrip("'").rstrip("'")

        # Split the line into a list
        line_lst = line.split()

        # Set each index to a key in a dictionary
        row = {
            'last': line_lst[0],
            'first': line_lst[1],
            'position': line_lst[2],
            'state': line_lst[3],
            'age': int(line_lst[4]),
            'salary': int(line_lst[5]),
            'education': line_lst[6],
            'exp': int(line_lst[7])
        }
        data.append(row)

######################################################################################################
print(
"""
Task (1):
    Create a sorted employee data file based on the ascending alphabet order of their last name.
"""
)

# Bubble sort the list according to last name
for i in range(0, len(data)):
    for j in range(0, len(data)-1):
        if data[j]['last'] > data[j+1]['last']:
            data[j], data[j+1] = data[j+1], data[j]
        else:
            continue
pretty_print(data)

# Output a file
print("File is also outputted as 'task_1.txt'")
with open('task_1.txt', 'w') as outf:
    for i in data:
        outf.write(f"{i['last']} {i['first']} {i['position']} {i['state']} {i['age']} {i['salary']} {i['education']} {i['exp']} \n")


######################################################################################################
print(
"""
Task (2):
    Print the data of top 5 highest salary employees in Iowa.
"""
)

# Gather all the salaries in Iowa
iowa_lst = []
for i in data:
    if i['state'] == 'IA':
        iowa_lst.append(i)
    else:
        continue

# Bubble sort the list according to salaries
for j in range(0, len(iowa_lst)):
    for i in range(0, len(iowa_lst)-1):
        if iowa_lst[i+1]['salary'] < iowa_lst[i]['salary']:
            iowa_lst[i], iowa_lst[i+1] = iowa_lst[i+1], iowa_lst[i]
        else:
            continue

# Select the top five
top_5 = iowa_lst[-5:]
pretty_print(top_5)


######################################################################################################
print(
"""
Task (3):
    Find the data of an employee whose first name is Sebastian and he is 53 years old. (Who is he?)
"""
)
# Search the entire list for Sebastian
for i in data:
    if i['first'] == 'Sebastian' and i['age'] == 53:
        sebastian = i
    else:
        continue

print(f"This is Sebastian: {sebastian}")

######################################################################################################
print(
"""
Task (4):
    Compare the average salaries of Senior Staff and Junior Staff.
"""
)

# Gather all the sr and jr salaries into list
sr_lst = []
jr_lst = []
for i in data:
    if i['position'] == 'Sr.Staff':
        sr_lst.append(i['salary'])
    elif i['position'] == 'Jr.Staff':
        jr_lst.append(i['salary'])
    else:
        continue

print(f"Average of Sr.Staff: {mean(sr_lst)}")
print(f"Average of Jr.Staff: {mean(jr_lst)}")
