# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
"""Most basic RNN: output = new_state = act(W * input + U * state + B)."""
_check_rnn_cell_input_dtypes([inputs, state])
gate_inputs = math_ops.matmul(
    array_ops.concat([inputs, state], 1), self._kernel)
gate_inputs = nn_ops.bias_add(gate_inputs, self._bias)
output = self._activation(gate_inputs)
exit((output, output))
