# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
cell = rnn_cell_impl.BasicRNNCell(5)
with self.assertRaisesRegex(ValueError,
                            "batch_size and dtype cannot be None"):
    cell.get_initial_state(None, None, None)

inputs = array_ops.placeholder(dtypes.float32, shape=(None, 4, 1))
with self.assertRaisesRegex(
    ValueError, "batch size from input tensor is different from"):
    cell.get_initial_state(inputs=inputs, batch_size=50, dtype=None)

with self.assertRaisesRegex(
    ValueError, "batch size from input tensor is different from"):
    cell.get_initial_state(
        inputs=inputs, batch_size=constant_op.constant(50), dtype=None)

with self.assertRaisesRegex(ValueError,
                            "dtype from input tensor is different from"):
    cell.get_initial_state(inputs=inputs, batch_size=None, dtype=dtypes.int16)

initial_state = cell.get_initial_state(
    inputs=inputs, batch_size=None, dtype=None)
self.assertEqual(initial_state.shape.as_list(), [None, 5])
self.assertEqual(initial_state.dtype, inputs.dtype)

batch = array_ops.shape(inputs)[0]
dtype = inputs.dtype
initial_state = cell.get_initial_state(None, batch, dtype)
self.assertEqual(initial_state.shape.as_list(), [None, 5])
self.assertEqual(initial_state.dtype, inputs.dtype)
