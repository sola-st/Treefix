# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sharding_util_ops_test.py
for dtype in self.numeric_types:
    with self.session() as sess, self.device_scope():
        concat = graph_fn(
            sess,
            input_values=[[[0, 1], [2, 3]]],
            input_dtype=dtype,
            num_concats=[1, 1],
            paddings=[0, -1])
        with self.assertRaisesOpError('non-negative, but got -1 at index 1'):
            sess.run(concat)
