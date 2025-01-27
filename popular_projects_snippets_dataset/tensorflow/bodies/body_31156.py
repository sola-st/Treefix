# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
"""Initialize the Multi-dimensional LSTM cell.

    Args:
      dims: tuple that contains the dimensions of the output of the cell,
      without including 'Time' or 'Batch' dimensions.
    """
if not isinstance(dims, tuple):
    raise TypeError("The dimensions passed to DummyMultiDimensionalLSTM "
                    "should be a tuple of ints.")
self._dims = dims
self._output_size = tensor_shape.TensorShape(self._dims)
self._state_size = (tensor_shape.TensorShape(self._dims),
                    tensor_shape.TensorShape(self._dims))
