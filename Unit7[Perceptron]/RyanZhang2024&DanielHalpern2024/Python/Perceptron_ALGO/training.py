import os
from random import randint, random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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
    sum = weights[1] * sat + weights[2] * gpa + weights[3] * essay + weights[4] * rec + weights[5] * extra + weights[0]
    if sum > 0:
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

learning_rate = 0.0001
max_epoch = 100000
errorList = []
epochs = []
epoch = 0
while True:
    epoch += 1
    r = randint(0, len(result)-1)
    if calculateOutput(weights, sat[r], gpa[r], essay[r], rec[r], extra[r]) > result[r]:
        weights[1] -= learning_rate * sat[r]
        weights[2] -= learning_rate * gpa[r]
        weights[3] -= learning_rate * essay[r]
        weights[4] -= learning_rate * rec[r]
        weights[5] -= learning_rate * extra[r]
        weights[0] -= learning_rate
    elif calculateOutput(weights, sat[r], gpa[r], essay[r], rec[r], extra[r]) < result[r]:
        weights[1] += learning_rate * sat[r]
        weights[2] += learning_rate * gpa[r]
        weights[3] += learning_rate * essay[r]
        weights[4] += learning_rate * rec[r]
        weights[5] += learning_rate * extra[r]
        weights[0] += learning_rate

    error = 0
    for i in range(0, len(result)):
        if result[i] != calculateOutput(weights, sat[i], gpa[i], essay[i], rec[i], extra[i]):
            error += 1

    # For graphs    
    errorList.append(100*(error/len(result)))
    epochs.append(epoch)
    
    # Print each epoch
    print("-----------------------------------------------------")
    print("Epoch {}:".format(epoch))
    print("Weights: w1 = {}, w2 = {}, w3 = {}, w4 = {}, w5 = {}, w0(bias) = {}".format(weights[1], weights[2], weights[3], weights[4], weights[5], weights[0]))
    print(f"Iteration: {epoch} Equation {weights[1]}*s + {weights[2]}*g + {weights[3]}*e + {weights[4]}*r + {weights[5]}*c + {weights[0]} = 0 \t ERR =", 100*(error/len(result)), "%")
    print("-----------------------------------------------------")
    
    #with open(f'./runs/training_output.txt', 'w') as f:
    #    f.write(f"Iteration: {epoch} Equation {weights[1]}*s + {weights[2]}*g + {weights[3]}*e + {weights[4]}*r + {weights[5]}*c + {weights[0]} = 0 \t ERR =", 100*(error/len(result)), "%\n")

    # if the epoch == max_epoch
    if epoch > max_epoch:
        break

try:
    run = os.listdir('./runs')[-1][0]
    with open(f'./runs/{int(run)+1}.txt', 'w') as f:
        f.write("{}, {}, {}, {}, {}, {}".format(weights[0], weights[1], weights[2], weights[3], weights[4], weights[5]))
except Exception as e:
    with open(f'./runs/1.txt', 'w') as f:
        f.write("{}, {}, {}, {}, {}, {}".format(weights[0], weights[1], weights[2], weights[3], weights[4], weights[5]))

#plotting graph

#sns.set_theme(style="darkgrid")

#setting up dataframe
#zipped = list(zip(errorList, epochs))
#df = pd.DataFrame(zipped, columns=['Error Rate', 'Iterations'])

#More complicated, but more customizable appearance (seaborn)        
#g = sns.relplot(x="Error Rate", y="Iterations", kind="line", data=df)
#g.figure.autofmt_xdate()
#plt.show()

#simple matplotlib
plt.plot(epochs, errorList)
plt.title('Error rate vs iterations')
plt.xlabel('Iterations')
plt.ylabel('Error rate (%)')
plt.show()

