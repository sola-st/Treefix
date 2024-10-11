# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sharding_util_ops_test.py
for dtype in self.numeric_types:
    with self.session() as sess, self.device_scope():
        concat = graph_fn(
            sess,
            input_values=[[0], [1, 2]],
            input_dtype=dtype,
            num_concats=[2])
        with self.assertRaisesOpError(
            r'same expected shape \[1\], but got \[2\] at index 1'):
            sess.run(concat)
