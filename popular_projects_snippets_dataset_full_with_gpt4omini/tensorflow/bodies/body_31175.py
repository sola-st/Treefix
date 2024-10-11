# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
cell = Plus1RNNCell()
batch_size = 2
input_size = 5
max_length = 8  # unrolled up to this length
inputs = max_length * [
    array_ops.placeholder(dtypes.float32, shape=(batch_size, input_size))
]
outputs, state = rnn.static_rnn(cell, inputs, dtype=dtypes.float32)
self.assertEqual(len(outputs), len(inputs))
for out, inp in zip(outputs, inputs):
    self.assertEqual(out.get_shape(), inp.get_shape())
    self.assertEqual(out.dtype, inp.dtype)

with self.session() as sess:
    input_value = np.random.randn(batch_size, input_size)
    values = sess.run(outputs + [state], feed_dict={inputs[0]: input_value})

    # Outputs
    for v in values[:-1]:
        self.assertAllClose(v, input_value + 1.0)

    # Final state
    self.assertAllClose(values[-1],
                        max_length * np.ones(
                            (batch_size, input_size), dtype=np.float32))
