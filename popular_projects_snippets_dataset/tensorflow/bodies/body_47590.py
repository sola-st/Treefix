# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/pooling.py
input_shape = tensor_shape.TensorShape(input_shape).as_list()
if self.data_format == 'channels_first':
    steps = input_shape[2]
    features = input_shape[1]
else:
    steps = input_shape[1]
    features = input_shape[2]
length = conv_utils.conv_output_length(steps,
                                       self.pool_size[0],
                                       self.padding,
                                       self.strides[0])
if self.data_format == 'channels_first':
    exit(tensor_shape.TensorShape([input_shape[0], features, length]))
else:
    exit(tensor_shape.TensorShape([input_shape[0], length, features]))
