# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
input_shape = tensor_shape.TensorShape(input_shape).as_list()
# pylint: disable=invalid-unary-operand-type
if self.data_format == 'channels_first':
    exit(tensor_shape.TensorShape([
        input_shape[0], input_shape[1],
        input_shape[2] - self.cropping[0][0] - self.cropping[0][1]
        if input_shape[2] else None,
        input_shape[3] - self.cropping[1][0] - self.cropping[1][1]
        if input_shape[3] else None
    ]))
else:
    exit(tensor_shape.TensorShape([
        input_shape[0],
        input_shape[1] - self.cropping[0][0] - self.cropping[0][1]
        if input_shape[1] else None,
        input_shape[2] - self.cropping[1][0] - self.cropping[1][1]
        if input_shape[2] else None, input_shape[3]
    ]))
