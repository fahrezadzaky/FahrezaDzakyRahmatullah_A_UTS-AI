"membuat program librabry numpy"
import numpy as np
"membuat program input untuk menambahkan nilai inputsnya"
inputs = [[1.2, 0.8, 0.5, 0.2, 0.1, 0.4],
					 [0.5, 0.91, 0.26, 0.5, 0.13, 0.15],
					 [0.26, 0.27, 0.17, 0.87, 0.77, 0.11],
                     [0.31, 0.33, 0.34, 0.35, 0.37, 0.38],
                     [0.21, 0.22, 0.23, 0.24, 0.25, 0.26],
                     [0.2, 0.8, 0.5, 0.2, 0.1, 0.4],
					 [0.5, 0.91, 0.26, 0.5, 0.13, 0.15],
					 [0.26, 0.27, 0.17, 0.87, 0.77, 0.11],
                     [0.31, 0.33, 0.34, 0.35, 0.37, 0.38],
                     [0.21, 0.22, 0.23, 0.24, 0.25, 0.26]]
"membuat program weight untuk menambahkan weightsnya"                     
weights = [[0.2, 0.8, 0.5, 0.2, 0.1, 0.4],
					 [0.5, 0.91, 0.26, 0.5, 0.13, 0.15],
					 [0.26, 0.27, 0.17, 0.87, 0.77, 0.11],
                     [0.31, 0.33, 0.34, 0.35, 0.37, 0.38],
                     [0.21, 0.22, 0.23, 0.24, 0.25, 0.26]]
"membuat bias untuk dijumlahkan dengan inputs dan weightnya"                     
biases = [2.0, 3.0, 0.5, 1.5, 2.0]
"membuat program layer ouput untuk mengetahui hasil ouputs dari operasi yang telah dibuat"
layer_outputs = np.dot(inputs, np.array(weights).T) + biases 
print(layer_outputs)