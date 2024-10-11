# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sharding_util_ops_test.py
num_splits = [2] * rank
num_outputs = 2 << (rank - 1)
input_value = np.reshape(np.arange(np.product(num_splits)), num_splits)
for dtype in self.numeric_types:
    with self.session() as sess, self.device_scope():
        split = graph_fn(
            sess,
            input_value=input_value,
            input_dtype=dtype,
            num_outputs=num_outputs,
            num_splits=num_splits)
        results = sess.run(split)
    self.assertLen(results, num_outputs)
    for i, result in enumerate(results):
        expected_output = np.reshape(i, [1] * rank).astype(dtype)
        self.assertAllClose(result, expected_output)
