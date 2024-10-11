# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sharding_util_ops_test.py
for dtype in self.numeric_types:
    with self.session() as sess, self.device_scope():
        concat = graph_fn(
            sess,
            input_values=[[0]],
            input_dtype=dtype,
            num_concats=[1],
            paddings=[2])
        with self.assertRaisesOpError(
            'exceed expected output shape dimension 1 at index 0, but got 2'):
            sess.run(concat)
