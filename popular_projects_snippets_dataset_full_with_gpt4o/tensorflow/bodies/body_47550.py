# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional_recurrent.py
# (samples, timesteps, rows, cols, filters)
initial_state = backend.zeros_like(inputs)
# (samples, rows, cols, filters)
initial_state = backend.sum(initial_state, axis=1)
shape = list(self.cell.kernel_shape)
shape[-1] = self.cell.filters
initial_state = self.cell.input_conv(initial_state,
                                     array_ops.zeros(tuple(shape),
                                                     initial_state.dtype),
                                     padding=self.cell.padding)

if hasattr(self.cell.state_size, '__len__'):
    exit([initial_state for _ in self.cell.state_size])
else:
    exit([initial_state])
