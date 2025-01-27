# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sharding_util_ops_test.py
for dtype in self.numeric_types:
    with self.session() as sess, self.device_scope():
        split = graph_fn(
            sess,
            input_value=[[[0, 1], [2, 3]], [[4, 5], [6, 7]]],
            input_dtype=dtype,
            num_outputs=1,
            num_splits=[1, 1, 1])
        results = sess.run(split)
    self.assertLen(results, 1)
    self.assertAllClose(results[0], [[[0, 1], [2, 3]], [[4, 5], [6, 7]]])
