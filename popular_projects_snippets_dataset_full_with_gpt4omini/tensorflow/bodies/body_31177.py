# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
cell = Plus1RNNCell()
sequence_length = array_ops.placeholder(dtypes.int64)
batch_size = 2
input_size = 5
max_length = 8
inputs = max_length * [
    array_ops.placeholder(dtypes.float32, shape=(batch_size, input_size))
]
with variable_scope.variable_scope("drop_scope"):
    dynamic_outputs, dynamic_state = rnn.static_rnn(
        cell, inputs, sequence_length=sequence_length, dtype=dtypes.float32)
self.assertEqual(len(dynamic_outputs), len(inputs))

with self.session() as sess:
    input_value = np.random.randn(batch_size, input_size)
    dynamic_values = sess.run(
        dynamic_outputs,
        feed_dict={
            inputs[0]: input_value,
            sequence_length: [2, 3]
        })
    dynamic_state_value = sess.run(
        [dynamic_state],
        feed_dict={
            inputs[0]: input_value,
            sequence_length: [2, 3]
        })

    # outputs are fully calculated for t = 0, 1
    for v in dynamic_values[:2]:
        self.assertAllClose(v, input_value + 1.0)

    # outputs at t = 2 are zero for entry 0, calculated for entry 1
    self.assertAllClose(dynamic_values[2],
                        np.vstack((np.zeros((input_size)),
                                   1.0 + input_value[1, :])))

    # outputs at t = 3+ are zero
    for v in dynamic_values[3:]:
        self.assertAllEqual(v, np.zeros_like(input_value))

    # the final states are:
    #  entry 0: the values from the calculation at t=1
    #  entry 1: the values from the calculation at t=2
    self.assertAllEqual(dynamic_state_value[0],
                        np.vstack((1.0 * (1 + 1) * np.ones((input_size)),
                                   1.0 * (2 + 1) * np.ones((input_size)))))
