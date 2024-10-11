# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
input_shape = tensor_shape.TensorShape(input_shape).as_list()
# pylint: disable=invalid-unary-operand-type
if self.data_format == 'channels_first':
    if input_shape[2] is not None:
        dim1 = input_shape[2] - self.cropping[0][0] - self.cropping[0][1]
    else:
        dim1 = None
    if input_shape[3] is not None:
        dim2 = input_shape[3] - self.cropping[1][0] - self.cropping[1][1]
    else:
        dim2 = None
    if input_shape[4] is not None:
        dim3 = input_shape[4] - self.cropping[2][0] - self.cropping[2][1]
    else:
        dim3 = None
    exit(tensor_shape.TensorShape(
        [input_shape[0], input_shape[1], dim1, dim2, dim3]))
elif self.data_format == 'channels_last':
    if input_shape[1] is not None:
        dim1 = input_shape[1] - self.cropping[0][0] - self.cropping[0][1]
    else:
        dim1 = None
    if input_shape[2] is not None:
        dim2 = input_shape[2] - self.cropping[1][0] - self.cropping[1][1]
    else:
        dim2 = None
    if input_shape[3] is not None:
        dim3 = input_shape[3] - self.cropping[2][0] - self.cropping[2][1]
    else:
        dim3 = None
    exit(tensor_shape.TensorShape(
        [input_shape[0], dim1, dim2, dim3, input_shape[4]]))
