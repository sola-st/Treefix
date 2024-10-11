# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/pooling.py
input_shape = tensor_shape.TensorShape(input_shape).as_list()
if self.data_format == 'channels_first':
    len_dim1 = input_shape[2]
    len_dim2 = input_shape[3]
    len_dim3 = input_shape[4]
else:
    len_dim1 = input_shape[1]
    len_dim2 = input_shape[2]
    len_dim3 = input_shape[3]
len_dim1 = conv_utils.conv_output_length(len_dim1, self.pool_size[0],
                                         self.padding, self.strides[0])
len_dim2 = conv_utils.conv_output_length(len_dim2, self.pool_size[1],
                                         self.padding, self.strides[1])
len_dim3 = conv_utils.conv_output_length(len_dim3, self.pool_size[2],
                                         self.padding, self.strides[2])
if self.data_format == 'channels_first':
    exit(tensor_shape.TensorShape(
        [input_shape[0], input_shape[1], len_dim1, len_dim2, len_dim3]))
else:
    exit(tensor_shape.TensorShape(
        [input_shape[0], len_dim1, len_dim2, len_dim3, input_shape[4]]))
