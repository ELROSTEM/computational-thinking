
import os


def normalize_gpa(gpa):
    """
    Normalize the gpa score
    :param gpa: gpa score
    :return: normalized gpa score
    """
    return (gpa) * 2.5

def normalize_sat(sat, max_sat, min_sat):
    """
    Normalize the SAT score
    :param sat: SAT score
    :param max_sat: maximum SAT score
    :param min_sat: minimum SAT score
    :return: normalized SAT score
    """
    return (10*((sat - 1200) / (1600 - 1200)))

def unnormalize_gpa(gpa):
    """
    Unnormalize the gpa score
    :param gpa: gpa score
    :return: unnormalized gpa score
    """
    return (gpa) / 2.5

def unnormalize_sat(sat):
    """
    Unnormalize the SAT score
    :param sat: SAT score
    :param max_sat: maximum SAT score
    :param min_sat: minimum SAT score
    :return: unnormalized SAT score
    """
    return (1200 + (1600 - 1200) * sat / 10)

def calculateOutput(weights, sat, gpa, essay, rec, extra):
    """
    Calculate the output of the perceptron
    :param weights: weights of the perceptron
    :param sat: SAT score
    :param gpa: GPA score
    :param essay: essay score
    :param rec: recommendation score
    :param extra: extra score
    :return: the output of the perceptron
    """

    sum =  weights[1] * sat + weights[2] * gpa + weights[3] * essay + weights[4] * rec + weights[5] * extra + weights[0]
    if sum >= 0:
        return 1, sum
    else:
        return -1, sum


########################################################################################################################
#                                                                                                                      # 
#                                               APP START                                                              #
#                                                                                                                      #
########################################################################################################################


# Data
sat = []
gpa = []
essay = []
rec = []
extra = []
result = []

# most recent run
with open(f'./outputs/weights.txt', 'r') as f:
    for row in f:
        weights = row.split()
        weights = [i.replace(',', '') for i in weights]
        weights = [float(i) for i in weights]
        
# Read the data from the file
with open('./inputs/testing.txt', 'r') as f:
    for row in f:
            row_lst = row.split()
            sat.append(float(row_lst[0]))
            gpa.append(float(row_lst[1]))
            essay.append(float(row_lst[2]))
            rec.append(float(row_lst[3]))
            extra.append(float(row_lst[4]))
            if row_lst[5] == 'A':
                result.append(1)
            else:
                result.append(-1)


# Normalize the sat score
for i in range(0, len(sat)):
    sat[i] = normalize_sat(sat[i], max(sat), min(sat))

# Normalize the gpa score
for i in range(0, len(gpa)):
    gpa[i] = normalize_gpa(gpa[i])

# Calculate the output
val = []
err = []
for i in range(0, len(result)):
    out, error = calculateOutput(weights, sat[i], gpa[i], essay[i], rec[i], extra[i])
    val.append(out)
    err.append(error)



incorrect = 0
for i in range(0, len(result)):
    if result[i] == val[i]:
        print('Correct')
    else:
        print(f'Incorrect: {err[i]}')
        incorrect += 1

print(f'Error Rate:', 100*(incorrect/len(result)))

outputList = []

with open(f'./outputs/testing_output.txt', 'w') as f:
    f.write(f"Descision Boundry: {weights[1]} * s + {weights[2]} * g + {weights[3]} * e + {weights[4]} * r + {weights[5]} * c + {weights[0]} = 0\n\n")
    for i in range(0, len(result)):
        if val[i] == 1:
            val[i] = 'A'
        else:
            val[i] = 'R'
    for i in range(0, len(result)):
        if result[i] == 1:
            result[i] = 'A'
        else:
            result[i] = 'R'

        if result[i] == val[i]:
            f.write(f"{i}) SAT: {unnormalize_sat(sat[i])} GPA: {unnormalize_gpa(gpa[i])} Essay: {essay[i]} Rec: {rec[i]} ExtraC: {extra[i]} Descison: {val[i]} Class: {result[i]}\n")
        else:
            f.write(f"{i}) SAT: {unnormalize_sat(sat[i])} GPA: {unnormalize_gpa(gpa[i])} Essay: {essay[i]} Rec: {rec[i]} ExtraC: {extra[i]} Descison: {val[i]} Class: {result[i]} *** ERROR\n")
    f.write(f"\nError Rate = {100*(incorrect/len(result))} %")
    
