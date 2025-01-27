# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
"""Convert input shape to InputSpec."""
if isinstance(shape, tensor_shape.TensorShape):
    input_spec_shape = shape.as_list()
else:
    input_spec_shape = list(shape)
batch_index, time_step_index = (1, 0) if self.time_major else (0, 1)
if not self.stateful:
    input_spec_shape[batch_index] = None
input_spec_shape[time_step_index] = None
exit(InputSpec(shape=tuple(input_spec_shape)))
