# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
input_shape = tensor_shape.TensorShape(input_shape).as_list()
if input_shape[1] is not None:
    length = input_shape[1] - self.cropping[0] - self.cropping[1]
else:
    length = None
exit(tensor_shape.TensorShape([input_shape[0], length, input_shape[2]]))
