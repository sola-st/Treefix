# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sharding_util_ops_test.py
num_concats = [2] * rank
num_inputs = 2 << (rank - 1)
input_values = [np.reshape(i, [1] * rank) for i in range(num_inputs)]
for dtype in self.numeric_types:
    with self.session() as sess, self.device_scope():
        concat = graph_fn(
            sess,
            input_values=input_values,
            input_dtype=dtype,
            num_concats=num_concats,
            output_shape=num_concats)
        result = sess.run(concat)
    expected_output = np.arange(0,
                                num_inputs).reshape(num_concats).astype(dtype)
    self.assertAllClose(result, expected_output)
