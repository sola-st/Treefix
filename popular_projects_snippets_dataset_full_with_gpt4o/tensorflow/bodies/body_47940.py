# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/cudnn_recurrent.py
# We invoke the base layer's initializer directly here because we do not
# want to create RNN cell instance.
super(RNN, self).__init__(**kwargs)  # pylint: disable=bad-super-call
self.return_sequences = return_sequences
self.return_state = return_state
self.go_backwards = go_backwards
self.stateful = stateful
self.time_major = time_major
self.supports_masking = False
self.input_spec = [InputSpec(ndim=3)]
if hasattr(self.cell.state_size, '__len__'):
    state_size = self.cell.state_size
else:
    state_size = [self.cell.state_size]
self.state_spec = [InputSpec(shape=(None, dim)) for dim in state_size]
self.constants_spec = None
self._states = None
self._num_constants = 0
self._vector_shape = constant_op.constant([-1])
