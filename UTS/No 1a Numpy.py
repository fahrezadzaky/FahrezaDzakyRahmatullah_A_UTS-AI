"MEMBUAT PROGRAM DENGAN LIBRABRY NUMPY"
import numpy as np
"MENAMBHKAN INPUT 10 LAYER"
inputs = [1.5, 2.5, 3.5, 2.8, 4.5, 5.5, 6.6, 7.0, 5.0, 4.0]
"MENAMBHKAN WEIGHT 1 NEURON 10 LAYERS"
weights = [0.15, 0.22, 0.11, 0.3, 0.4, 0.7, 0.8, 0.10, 0.2, 0.3]
"MENAMBHKAN BIAS SESUAI DENGAN NEURON"
bias = 5.0
outputs = np.dot(weights, inputs) + bias
print(outputs)