from random import randint, random


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
weights = [random()*10, random()*10, random()*10, random()*10, random()*10, random()*10]

# Read the data from the file
with open('training.txt', 'r') as f:
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

learning_rate = 0.001
max_epoch = 10000

epoch = 0
while True:
    epoch += 1

    r = randint(0, len(result)-1)
    if result[r] < 1:
        weights[1] -= learning_rate * sat[r]
        weights[2] -= learning_rate * gpa[r]
        weights[3] -= learning_rate * essay[r]
        weights[4] -= learning_rate * rec[r]
        weights[5] -= learning_rate * extra[r]
        weights[0] -= learning_rate
    elif result[r] > -1:
        weights[1] += learning_rate * sat[r]
        weights[2] += learning_rate * gpa[r]
        weights[3] += learning_rate * essay[r]
        weights[4] += learning_rate * rec[r]
        weights[5] += learning_rate * extra[r]
        weights[0] += learning_rate

    # Print each epoch
    print("-----------------------------------------------------")
    print("Epoch {}:".format(epoch))
    print("Weights: w1 = {}, w2 = {}, w3 = {}, w4 = {}, w5 = {}, w0(bias) = {}".format(weights[1], weights[2], weights[3], weights[4], weights[5], weights[0]))
    print("-----------------------------------------------------")

    # if the epoch == max_epoch
    if epoch == max_epoch:
        break
    else:
        continue


with open('weights.txt', 'w') as f:
    f.write("{}, {}, {}, {}, {}, {}".format(weights[0], weights[1], weights[2], weights[3], weights[4], weights[5]))


