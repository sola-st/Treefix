# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/rnn_cell_wrapper_v2.py
"""Runs the RNN cell step computation.

    When `call` is being used, we assume that the wrapper object has been built,
    and therefore the wrapped cells has been built via its `build` method and
    its `call` method can be used directly.

    This allows to use the wrapped cell and the non-wrapped cell equivalently
    when using `call` and `build`.

    Args:
      inputs: A tensor with wrapped cell's input.
      state: A tensor or tuple of tensors with wrapped cell's state.
      **kwargs: Additional arguments passed to the wrapped cell's `call`.

    Returns:
      A pair containing:

      - Output: A tensor with cell's output.
      - New state: A tensor or tuple of tensors with new wrapped cell's state.
    """
exit(self._call_wrapped_cell(
    inputs, state, cell_call_fn=self.cell.call, **kwargs))
