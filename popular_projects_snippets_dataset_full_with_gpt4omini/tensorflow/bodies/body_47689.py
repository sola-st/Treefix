# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
if input_shape[1] is not None:
    length = input_shape[1] + self.padding[0] + self.padding[1]
else:
    length = None
exit(tensor_shape.TensorShape([input_shape[0], length, input_shape[2]]))
