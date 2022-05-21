
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

# most recent run
with open(f'./outputs/weights.txt', 'r') as f:
    for row in f:
        weights = row.split()
        weights = [i.replace(',', '') for i in weights]
        weights = [float(i) for i in weights]
        
# Read the data from the file
with open('./inputs/application.txt', 'r') as f:
    for row in f:
            row_lst = row.split()
            sat.append(float(row_lst[0]))
            gpa.append(float(row_lst[1]))
            essay.append(float(row_lst[2]))
            rec.append(float(row_lst[3]))
            extra.append(float(row_lst[4]))


# Normalize the sat score
for i in range(0, len(sat)):
    sat[i] = normalize_sat(sat[i], max(sat), min(sat))

# Normalize the gpa score
for i in range(0, len(gpa)):
    gpa[i] = normalize_gpa(gpa[i])

# Calculate the output
val = []
for i in range(0, len(sat)):
    out, error = calculateOutput(weights, sat[i], gpa[i], essay[i], rec[i], extra[i])
    val.append(out)

with open(f'./outputs/deploy_output.txt', 'w') as f:
    for i in range(0, len(val)):
        if val[i] == 1:
            val[i] = 'A'
        else:
            val[i] = 'R'
        f.write(f"{i}) SAT: {unnormalize_sat(sat[i])} GPA: {unnormalize_gpa(gpa[i])} Essay: {essay[i]} Rec: {rec[i]} ExtraC: {extra[i]} Prediction: {val[i]}\n")
        print(f"{i}) SAT: {unnormalize_sat(sat[i])} GPA: {unnormalize_gpa(gpa[i])} Essay: {essay[i]} Rec: {rec[i]} ExtraC: {extra[i]} Prediction: {val[i]}")
    
