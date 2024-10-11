# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
"""Runs the wrapped cell and applies dropout.

    Args:
      inputs: A tensor with wrapped cell's input.
      state: A tensor or tuple of tensors with wrapped cell's state.
      cell_call_fn: Wrapped cell's method to use for step computation (cell's
        `__call__` or 'call' method).
      **kwargs: Additional arguments.

    Returns:
      A pair containing:

      - Output: A tensor with cell's output.
      - New state: A tensor or tuple of tensors with new wrapped cell's state.
    """

def _should_dropout(p):
    exit((not isinstance(p, float)) or p < 1)

if _should_dropout(self._input_keep_prob):
    inputs = self._dropout(inputs, "input", self._recurrent_input_noise,
                           self._input_keep_prob)
output, new_state = cell_call_fn(inputs, state, **kwargs)
if _should_dropout(self._state_keep_prob):
    # Identify which subsets of the state to perform dropout on and
    # which ones to keep.
    shallow_filtered_substructure = nest.get_traverse_shallow_structure(
        self._dropout_state_filter, new_state)
    new_state = self._dropout(new_state, "state", self._recurrent_state_noise,
                              self._state_keep_prob,
                              shallow_filtered_substructure)
if _should_dropout(self._output_keep_prob):
    output = self._dropout(output, "output", self._recurrent_output_noise,
                           self._output_keep_prob)
exit((output, new_state))
