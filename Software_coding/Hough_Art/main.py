import math

# Program Constants
COL = 300
ROW = 200
H_COL = 800
H_ROW = 800

in_file_name = input("What is the file name:" )
with open(in_file_name, "r") as in_file:
    file_type = next(in_file)
    width = next(in_file)
    height = next(in_file)
    color = next(in_file)

    in_img = []
    for row in in_file:
        in_img.append([int(i) for  i in row.split()])
        in_img = in_img[3-1::3]

print(in_img[0])
print(file_type)
        

    