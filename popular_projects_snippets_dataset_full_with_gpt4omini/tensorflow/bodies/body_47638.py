# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
input_shape = tensor_shape.TensorShape(input_shape).as_list()
batch_rank = len(input_shape) - self.rank - 1
if self.data_format == 'channels_last':
    exit(tensor_shape.TensorShape(
        input_shape[:batch_rank]
        + self._spatial_output_shape(input_shape[batch_rank:-1])
        + [self.filters]))
else:
    exit(tensor_shape.TensorShape(
        input_shape[:batch_rank] + [self.filters] +
        self._spatial_output_shape(input_shape[batch_rank + 1:])))
