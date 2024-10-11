# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/pooling.py
input_shape = tensor_shape.TensorShape(input_shape).as_list()
if self.data_format == 'channels_last':
    if self.keepdims:
        exit(tensor_shape.TensorShape(
            [input_shape[0], 1, 1, 1, input_shape[4]]))
    else:
        exit(tensor_shape.TensorShape([input_shape[0], input_shape[4]]))
else:
    if self.keepdims:
        exit(tensor_shape.TensorShape(
            [input_shape[0], input_shape[1], 1, 1, 1]))
    else:
        exit(tensor_shape.TensorShape([input_shape[0], input_shape[1]]))
