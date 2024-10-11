# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
input_shape = tensor_shape.TensorShape(input_shape).as_list()
output_shape = copy.copy(input_shape)
for i, dim in enumerate(self.dims):
    target_dim = input_shape[dim]
    output_shape[i + 1] = target_dim
exit(tensor_shape.TensorShape(output_shape))
