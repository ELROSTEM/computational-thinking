import math

# Program Constants
COL = 300
ROW = 200
H_COL = 800
H_ROW = 800

# Manipulatable variables
amplitude = 2.5
frequency = 1.0
phase_x = 0.0
phase_y = 0.0

# Image lists
img_inp = []
hough = [ [ 0 for y in range(H_COL) ] for x in range(H_ROW) ]

# Read input file
in_file_name = input("What is the file name:" )
with open(in_file_name, "r") as in_file:
    file_type = next(in_file)
    width, height = next(in_file).split()
    ppm_color = next(in_file)

    for row in in_file:
        row_lst = [int(i) for  i in row.split()]
        color_row = row_lst[3-1::3]
        img_inp.append(color_row)

# Create Hough Space
for i in range(ROW):
    for j in range(COL):
        if img_inp[i][j] == int(ppm_color):
            x = j - COL/2
            y = i - ROW/2
            for t in range(H_COL):
                r = amplitude*(x*math.cos(2.0*math.pi*frequency*t/H_COL - phase_x) + y*math.sin(2.0*math.pi*frequency*t/H_COL - phase_y));
                xx = r * math.cos(2.0*math.pi*t/H_COL - phase_x);
                yy = r * math.sin(2.0*math.pi*t/H_ROW - phase_y);
                if xx >= -H_COL/2 and xx < H_COL/2 and yy >= -H_ROW/2 and yy < H_ROW/2:
                    hough[int(xx+H_COL/2)][int(yy+H_ROW/2)] = hough[int(xx+H_COL/2)][int(yy+H_ROW/2)] + 1

# Write into art.ppm
with open("py_art.ppm", "w") as out_file:
    out_file.write(f"{file_type}{str(H_COL)} {str(H_ROW)} {ppm_color}")
    for i in range(H_ROW):
        for j in range(H_COL):
            out_file.write(f"{int(hough[i][j]*(1.0 + i/23.0))} {int(hough[i][j]*(H_COL - j)/20)} {int(hough[i][j]*(H_ROW - j)/30)} ")

print("Success") 
        

    