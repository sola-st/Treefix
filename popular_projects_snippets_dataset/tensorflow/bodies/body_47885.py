# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
input_shape = tensor_shape.TensorShape(input_shape).as_list()
if not input_shape:
    output_shape = tensor_shape.TensorShape([1])
else:
    output_shape = [input_shape[0]]
if np.all(input_shape[1:]):
    output_shape += [np.prod(input_shape[1:], dtype=int)]
else:
    output_shape += [None]
exit(tensor_shape.TensorShape(output_shape))
