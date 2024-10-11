# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
cell = Plus1RNNCell()
full_dropout_cell = rnn_cell.DropoutWrapper(
    cell, input_keep_prob=1e-6, seed=0)
self.assertIn("cell", full_dropout_cell._trackable_children())
self.assertIs(full_dropout_cell._trackable_children()["cell"], cell)
batch_size = 2
input_size = 5
max_length = 8
inputs = max_length * [
    array_ops.placeholder(dtypes.float32, shape=(batch_size, input_size))
]
with variable_scope.variable_scope("share_scope"):
    outputs, state = rnn.static_rnn(cell, inputs, dtype=dtypes.float32)
with variable_scope.variable_scope("drop_scope"):
    dropped_outputs, _ = rnn.static_rnn(
        full_dropout_cell, inputs, dtype=dtypes.float32)
self.assertEqual(len(outputs), len(inputs))
for out, inp in zip(outputs, inputs):
    self.assertEqual(out.get_shape().as_list(), inp.get_shape().as_list())
    self.assertEqual(out.dtype, inp.dtype)

with self.session() as sess:
    input_value = np.random.randn(batch_size, input_size)
    values = sess.run(outputs + [state], feed_dict={inputs[0]: input_value})
    full_dropout_values = sess.run(
        dropped_outputs, feed_dict={
            inputs[0]: input_value
        })

    for v in values[:-1]:
        self.assertAllClose(v, input_value + 1.0)
    for d_v in full_dropout_values[:-1]:  # Add 1.0 to dropped_out (all zeros)
        self.assertAllClose(d_v, np.ones_like(input_value))
