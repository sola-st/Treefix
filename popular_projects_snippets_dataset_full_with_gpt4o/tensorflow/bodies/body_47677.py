# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
input_shape = tensor_shape.TensorShape(input_shape).as_list()
size = self.size * input_shape[1] if input_shape[1] is not None else None
exit(tensor_shape.TensorShape([input_shape[0], size, input_shape[2]]))
