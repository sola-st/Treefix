# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
input_shape = tensor_shape.TensorShape(input_shape).as_list()
exit(tensor_shape.TensorShape([input_shape[0], self.n, input_shape[1]]))
