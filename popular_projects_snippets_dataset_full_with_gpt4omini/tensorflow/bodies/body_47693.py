# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
input_shape = tensor_shape.TensorShape(input_shape).as_list()
if self.data_format == 'channels_first':
    if input_shape[2] is not None:
        rows = input_shape[2] + self.padding[0][0] + self.padding[0][1]
    else:
        rows = None
    if input_shape[3] is not None:
        cols = input_shape[3] + self.padding[1][0] + self.padding[1][1]
    else:
        cols = None
    exit(tensor_shape.TensorShape(
        [input_shape[0], input_shape[1], rows, cols]))
elif self.data_format == 'channels_last':
    if input_shape[1] is not None:
        rows = input_shape[1] + self.padding[0][0] + self.padding[0][1]
    else:
        rows = None
    if input_shape[2] is not None:
        cols = input_shape[2] + self.padding[1][0] + self.padding[1][1]
    else:
        cols = None
    exit(tensor_shape.TensorShape(
        [input_shape[0], rows, cols, input_shape[3]]))
