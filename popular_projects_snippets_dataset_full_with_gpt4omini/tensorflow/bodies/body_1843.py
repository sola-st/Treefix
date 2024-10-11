# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sharding_util_ops_test.py
for dtype in self.numeric_types:
    with self.session() as sess, self.device_scope():
        concat = graph_fn(
            sess, input_values=[[0, 1]], input_dtype=dtype, num_concats=[2])
        with self.assertRaisesOpError('\'N\' must match number of slices 2'):
            sess.run(concat)
