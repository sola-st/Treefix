# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
cell = Plus1RNNCell()
in_eager_mode = context.executing_eagerly()
# With static batch size
if in_eager_mode:
    inputs = np.zeros((3, 4, 5), dtype=np.float32)
    initial_state = np.zeros((3, 5), dtype=np.float32)
else:
    inputs = array_ops.placeholder(dtypes.float32, shape=(3, 4, 5))
    initial_state = array_ops.placeholder(dtypes.float32, shape=(3, 5))

# - Without initial_state
outputs, state = rnn.dynamic_rnn(cell, inputs, dtype=dtypes.float32)
self.assertEqual(3, outputs.shape[0])
self.assertEqual(3, state.shape[0])

# - With initial_state
outputs, state = rnn.dynamic_rnn(
    cell, inputs, initial_state=initial_state)
self.assertEqual(3, outputs.shape[0])
self.assertEqual(3, state.shape[0])

# Without static batch size
# Tensor shapes are fully determined with eager execution enabled,
# so only run this test for graph construction.
if not in_eager_mode:
    inputs = array_ops.placeholder(dtypes.float32, shape=(None, 4, 5))
    # - Without initial_state
    outputs, state = rnn.dynamic_rnn(cell, inputs, dtype=dtypes.float32)
    self.assertEqual(None, outputs.shape.dims[0].value)
    self.assertEqual(None, state.shape.dims[0].value)
    # - With initial_state
    outputs, state = rnn.dynamic_rnn(
        cell,
        inputs,
        initial_state=array_ops.placeholder(dtypes.float32, shape=(None, 5)))
    self.assertEqual(None, outputs.shape.dims[0].value)
    self.assertEqual(None, state.shape.dims[0].value)
