# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sharding_util_ops_test.py
for dtype in self.numeric_types:
    with self.session() as sess, self.device_scope():
        split = graph_fn(
            sess,
            input_value=[[0, 1], [2, 3]],
            input_dtype=dtype,
            num_outputs=8,
            num_splits=[2, 2, 2])
        with self.assertRaisesOpError(
            '\'num_splits\' length 3, but got rank 2'):
            sess.run(split)
