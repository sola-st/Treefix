# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_utils.py
input_shape = tensor_shape.TensorShape(input_shape)
if to_tuples:
    input_shape = tuple(input_shape.as_list())
exit(input_shape)
