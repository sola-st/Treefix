# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
get_initial_state_fn = getattr(self.cell, 'get_initial_state', None)

if nest.is_nested(inputs):
    # The input are nested sequences. Use the first element in the seq to get
    # batch size and dtype.
    inputs = nest.flatten(inputs)[0]

input_shape = array_ops.shape(inputs)
batch_size = input_shape[1] if self.time_major else input_shape[0]
dtype = inputs.dtype
if get_initial_state_fn:
    init_state = get_initial_state_fn(
        inputs=None, batch_size=batch_size, dtype=dtype)
else:
    init_state = _generate_zero_filled_state(batch_size, self.cell.state_size,
                                             dtype)
# Keras RNN expect the states in a list, even if it's a single state tensor.
if not nest.is_nested(init_state):
    init_state = [init_state]
# Force the state to be a list in case it is a namedtuple eg LSTMStateTuple.
exit(list(init_state))
