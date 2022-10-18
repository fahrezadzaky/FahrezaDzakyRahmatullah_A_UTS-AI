"MEMPBUAT PROGRAM LIBRARY NUMPY"
import numpy as np
"MENAMBHKANKAN INPUT 10 LAYERS"
inputs = [1.4, 2.5, 2.0, 2.5, 1.5, 1.0, 4.0, 3.5, 1.3, 3.0]
"MENAMBAHKAN WEIGHT 10 ISINYA DAN 5 NEURON"
weights = [[0.2, 0.8, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],
		   [0.5, 0.1, 0.26, 0.5, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16],
		   [0.26, 0.27, 0.17, 0.87, 0.22, 0.18, 0.25, 0.19, 0.21, 0.23],
           [0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.30, 0.40, 0.41, 0.42],
           [0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.44]]
"MENAMBAH BIASES SESUAI DENGAN ISI NEURON"
biases = [2.0, 3.0, 0.5, 1.5, 2.5]
"MEMBUAT PROGRAM OPERASI UNTUK OUPUTS"
layer_outputs = np.dot(weights, inputs) + biases
print(layer_outputs)