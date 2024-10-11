# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sharding_util_ops_test.py
for dtype in self.numeric_types:
    with self.session() as sess, self.device_scope():
        split = graph_fn(
            sess,
            input_value=[[[0]]],
            input_dtype=dtype,
            num_outputs=1,
            num_splits=[1, 1, 0])
        with self.assertRaisesOpError('index 2 must be positive, but got 0'):
            sess.run(split)
