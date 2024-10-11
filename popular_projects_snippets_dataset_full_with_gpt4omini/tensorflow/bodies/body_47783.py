# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
"""Long short-term memory cell (LSTM).

    Args:
      inputs: `2-D` tensor with shape `[batch_size, input_size]`.
      state: An `LSTMStateTuple` of state tensors, each shaped `[batch_size,
        num_units]`, if `state_is_tuple` has been set to `True`.  Otherwise, a
        `Tensor` shaped `[batch_size, 2 * num_units]`.

    Returns:
      A pair containing the new hidden state, and the new state (either a
        `LSTMStateTuple` or a concatenated state, depending on
        `state_is_tuple`).
    """
_check_rnn_cell_input_dtypes([inputs, state])

sigmoid = math_ops.sigmoid
one = constant_op.constant(1, dtype=dtypes.int32)
# Parameters of gates are concatenated into one multiply for efficiency.
if self._state_is_tuple:
    c, h = state
else:
    c, h = array_ops.split(value=state, num_or_size_splits=2, axis=one)

gate_inputs = math_ops.matmul(
    array_ops.concat([inputs, h], 1), self._kernel)
gate_inputs = nn_ops.bias_add(gate_inputs, self._bias)

# i = input_gate, j = new_input, f = forget_gate, o = output_gate
i, j, f, o = array_ops.split(
    value=gate_inputs, num_or_size_splits=4, axis=one)

forget_bias_tensor = constant_op.constant(self._forget_bias, dtype=f.dtype)
# Note that using `add` and `multiply` instead of `+` and `*` gives a
# performance improvement. So using those at the cost of readability.
add = math_ops.add
multiply = math_ops.multiply
new_c = add(
    multiply(c, sigmoid(add(f, forget_bias_tensor))),
    multiply(sigmoid(i), self._activation(j)))
new_h = multiply(self._activation(new_c), sigmoid(o))

if self._state_is_tuple:
    new_state = LSTMStateTuple(new_c, new_h)
else:
    new_state = array_ops.concat([new_c, new_h], 1)
exit((new_h, new_state))
