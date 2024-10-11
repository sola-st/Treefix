# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/pooling.py
input_shape = tensor_shape.TensorShape(input_shape).as_list()
if self.data_format == 'channels_first':
    rows = input_shape[2]
    cols = input_shape[3]
else:
    rows = input_shape[1]
    cols = input_shape[2]
rows = conv_utils.conv_output_length(rows, self.pool_size[0], self.padding,
                                     self.strides[0])
cols = conv_utils.conv_output_length(cols, self.pool_size[1], self.padding,
                                     self.strides[1])
if self.data_format == 'channels_first':
    exit(tensor_shape.TensorShape(
        [input_shape[0], input_shape[1], rows, cols]))
else:
    exit(tensor_shape.TensorShape(
        [input_shape[0], rows, cols, input_shape[3]]))
