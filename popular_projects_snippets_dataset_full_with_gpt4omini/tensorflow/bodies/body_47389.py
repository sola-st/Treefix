# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
if isinstance(shape, tensor_shape.TensorShape):
    shape = tuple(shape.as_list())
# remove the timestep from the input_shape
exit(shape[1:] if self.time_major else (shape[0],) + shape[2:])
