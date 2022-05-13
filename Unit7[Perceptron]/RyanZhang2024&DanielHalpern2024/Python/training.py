from random import random


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
    return (10*((sat - min_sat) / (max_sat - min_sat)))

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
        return 1
    else:
        return -1


########################################################################################################################
#                                                                                                                      # 
#                                               APP START                                                              #
#                                                                                                                      #
########################################################################################################################


# Training Data
sat = []
gpa = []
essay = []
rec = []
extra = []
result = []

# Weights
weights = [random(), random(), random(), random(), random(), random()]

# Read the data from the file
with open('data.txt', 'r') as f:
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

print("Initial Weights: w1 = {}, w2 = {}, w3 = {}, w4 = {}, w5 = {}, w0(bias) = {} \n".format(weights[1], weights[2], weights[3], weights[4], weights[5], weights[0]))

epoch = 0
learning_rate = 0.1

while True:
    epoch += 1
    global_error = 0
    for i in range(0, len(result)):
        output = calculateOutput(weights, sat[i], gpa[i], essay[i], rec[i], extra[i])

        # Calculate the error
        local_error = result[i] - output

        # Update the weights
        weights[1] += learning_rate * local_error * sat[i]
        weights[2] += learning_rate * local_error * gpa[i]
        weights[3] += learning_rate * local_error * essay[i]
        weights[4] += learning_rate * local_error * rec[i]
        weights[5] += learning_rate * local_error * extra[i]
        weights[0] += learning_rate * local_error

        # Update global error
        global_error += local_error**2

    # Root Mean Square Error
    print("-----------------------------------------------------")
    print("Epoch {}: RMSE = {} ".format(epoch, (global_error/len(result))**0.5))
    print("Weights: w1 = {}, w2 = {}, w3 = {}, w4 = {}, w5 = {}, w0(bias) = {}".format(weights[1], weights[2], weights[3], weights[4], weights[5], weights[0]))
    print("-----------------------------------------------------")

    # Break if the error is == 0
    if global_error == 0 or epoch == 10000:
        break
    else:
        continue



