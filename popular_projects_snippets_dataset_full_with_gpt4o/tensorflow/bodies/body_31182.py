# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
# Test case for GitHub issue 16228
# Not passing dtype in constructor results in default float32
lstm = rnn_cell.LSTMCell(10)
input_tensor = array_ops.ones([10, 50])
lstm.build(input_tensor.get_shape())
self.assertEqual(lstm._bias.dtype.base_dtype, dtypes.float32)

# Explicitly pass dtype in constructor
for dtype in [dtypes.float16, dtypes.float32, dtypes.float64]:
    lstm = rnn_cell.LSTMCell(10, dtype=dtype)
    input_tensor = array_ops.ones([10, 50])
    lstm.build(input_tensor.get_shape())
    self.assertEqual(lstm._bias.dtype.base_dtype, dtype)
