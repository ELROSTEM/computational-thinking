from random import randint, random

# Plotting libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def normalizeType(type):
    """
    Normalize the type of the apartment
    :param type: type of the apartment
    :return: the normalized type
    """
    if type == 'coop':
        return 0
    else:
        return 1

def normalizeBedroom(bedroom):
    """
    Normalize the number of bedrooms
    :param bedroom: number of bedrooms
    :return: the normalized number of bedrooms
    """
    return (bedroom - 1)/6

def normalizeBathroom(bathroom):
    """
    Normalize the number of bathrooms
    :param bathroom: number of bathrooms
    :return: the normalized number of bathrooms
    """
    return (bathroom - 1)/5

def normalizeLivingroom(livingroom):
    """
    Normalize the number of livingrooms
    :param livingroom: number of livingrooms
    :return: the normalized number of livingrooms
    """
    return (livingroom)/2

def normalizeDiningroom(diningroom):
    """
    Normalize the number of diningrooms
    :param diningroom: number of diningrooms
    :return: the normalized number of diningrooms
    """
    return diningroom 

def normalizeCondition(condition):
    """
    Normalize the condition of the apartment
    :param condition: condition of the apartment
    :return: the normalized condition
    """
    return (condition - 2)/3

def normalizeArea(area):
    """
    Normalize the area of the apartment
    :param area: area of the apartment
    :return: the normalized area
    """
    return (area-900)/3600


def calculateOutput(weights, house, error):
    """
    Calculate the output of the perceptron
    :param weights: weights of the perceptron
    :param house: house matrix
    :param error: error matrix
    :return: the output of the perceptron
    """

    output = np.add(np.matmul(house , weights), error)

    return output
    


########################################################################################################################
#                                                                                                                      # 
#                                               APP START                                                              #
#                                                                                                                      
# TO DO LIST:                                                                                                          #
#   X Work on constant term which is column 6 whcih is all ones                                                        #                                 
#   - work on normalizing the price                                                                                    #
########################################################################################################################


# Training Data

type = []
bedroom = []
bathroom = []
livingroom = []
diningroom = []
condition = []
area = []
bias = []
price = []
house = []

# Weights
weights = [random()*10, random()*10, random()*10, random()*10, random()*10, random()*10, random()*10, random()*10]
startingWeights = weights

# Read the data from the file
with open('./inputs/training.txt', 'r') as f:
    for row in f:
            row_lst = row.split()
            type.append(row_lst[0])
            bedroom.append(float(row_lst[1]))
            bathroom.append(float(row_lst[2]))
            livingroom.append(float(row_lst[3]))
            diningroom.append(float(row_lst[4]))
            condition.append(float(row_lst[5]))
            area.append(float(row_lst[6]))
            bias.append(1)
            price.append(float(row_lst[7]))


# Normalize the values
for i in range(0, len(type)):
    type[i] = normalizeType(type[i])
    bedroom[i] = normalizeBedroom(bedroom[i])
    bathroom[i] = normalizeBathroom(bathroom[i])
    livingroom[i] = normalizeLivingroom(livingroom[i])
    diningroom[i] = normalizeDiningroom(diningroom[i])
    condition[i] = normalizeCondition(condition[i])
    area[i] = normalizeArea(area[i])
    house.append([type[i], bedroom[i], bathroom[i], livingroom[i], diningroom[i], condition[i], area[i], bias[i]])


#Matrixing
house = np.matrix(house)
weights = np.matrix(np.vstack(np.array(weights)))
error = np.matrix(np.zeros((len(house), 1)))

# Training Loop
learning_rate = 0.0025
max_epoch = 100000
epoch = 0
while epoch < max_epoch:
    epoch += 1

    output = calculateOutput(weights, house, error)

    # Calculate the Mean Squared Error
    sum_error = 0
    error_lst = []
    for i in range(0, len(price)):
        sum_error += (output[i, 0] - price[i])**2
        error_lst.append(output[i, 0] - price[i])
    
    error = np.matrix(np.vstack(np.array(error_lst)))
    mean_square_error = sum_error/800

    # Calculate the Gradient
    gradient = np.matmul(house.transpose(), error)
    weights = np.add(weights, ((learning_rate/800) * gradient))

    print(f"Epoch: {epoch} | MSE: {mean_square_error}")
    print(f"New weights: ", weights)

#with open(f'./outputs/weights.txt', 'w') as f:
#    f.write("{}, {}, {}, {}, {}, {}".format(weights[0], weights[1], weights[2], weights[3], weights[4], weights[5]))

#with open(f'./outputs/errors.txt', 'w') as f:
#    for i in range(0, len(errorList)):
#        f.write(f"{errorList[i]}\n")

#with open(f'./outputs/training_output.txt', 'w') as f:
#    f.write(f"Initial Equation : {weights[1]}*s + {weights[2]}*g + {weights[3]}*e + {weights[4]}*r + {weights[5]}*c + {weights[0]} = 0\n\n")
#    for i in range(0, len(trainingOut_list)):
#        f.write(f"{trainingOut_list[i]}\n")
#    f.write(f"\nFinal Equation: {trainingOut_list[len(trainingOut_list)-1]}")


# plotting graph

# sns.set_theme(style="darkgrid")

# # setting up dataframe
# zipped = list(zip(errorList, epochs))
# df = pd.DataFrame(zipped, columns=['Error Rate', 'Iterations'])

# # More complicated, but more customizable appearance (seaborn)        
# g = sns.relplot(x="Error Rate", y="Iterations", kind="line", data=df)
# g.figure.autofmt_xdate()
# plt.show()

# #simple matplotlib
# plt.plot(epochs, errorList)
# plt.title('Error rate vs iterations')
# plt.xlabel('Iterations')
# plt.ylabel('Error rate (%)')
# plt.show()

