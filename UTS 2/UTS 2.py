#   membuat program untuk inisialisasi numpy
import numpy as np

# membuat program untuk variabel inputs
inputs	=  [[2.2, 3.5, 7, 4, 2, 4.5, 3.2 , 5, 1.5, 2.2],
            [1.1, 3.7, 2.3, 2.2, 2.7, 4.3, 1.7, 2.3, 3.5, 1.3],
            [2.6, 1.6, 1.3, 2.1, 2.0, 2.5, 1.2, 3.2, 2.4, 4.0],
            [2.3, 4.1, 3.4, 1.8, 3.2, 1.35, 2.1, 1.0, 2.2, 3.6],
            [3.3, 2.0, 4.5, 3.3, 3.5, 2.6, 4.6, 2.8, 5.5, 5.5],
            [1.2, 1.7, 1.6, 1.5, 1.2, 1.2, 1.3, 2.3, 1.5, 1.4]]

# membuat progarm weights untuk hidden layer 1 
weights =  [[0.3, 0.2, 0.8, 0.9, 0.10, 0.11, 0.11, 0.12, 0.13, 0.14],
            [0.20, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29],
            [0.30, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39],
            [0.40, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49],
            [0.50, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59]]

#membuat bias hidden layer 1
bias = [7, 3, 5, 6, 4]

#membuat program output hidden layer 1
output  = np.dot(inputs, np.array(weights).T) + bias

# membuat program untuk weights hidden layer 2
weights2 = [[0.1, 0.2, 0.3, 0.4, 0.5],
            [0.77, 0.88, 0.66, 0.33, 0.44],
            [0.38, 0.34, 0.41, 0.43, 0.22]]

# membuat bias hidden layer 2
bias2 = [2, 5, 5]

#membuat program output hidden layer 2
output2 = np.dot(output, np.array(weights2).T) + bias2	

# menyetak output
print(output2)