# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sharding_util_ops_test.py
for dtype in self.numeric_types:
    with self.session() as sess, self.device_scope():
        concat = graph_fn(
            sess, input_values=[[0]], input_dtype=dtype, num_concats=[1, 1])
        with self.assertRaisesOpError(
            '\'num_concats\' length 2, but got rank 1'):
            sess.run(concat)
