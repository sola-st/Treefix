# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sharding_util_ops_test.py
for dtype in self.numeric_types:
    with self.session() as sess, self.device_scope():
        concat = graph_fn(
            sess,
            input_values=[[[[0, 1], [2, 3]], [[4, 5], [6, 7]]]],
            input_dtype=dtype,
            num_concats=[1, 1, 1],
            output_shape=[1, 1, 1],
            paddings=[1, 1, 1])
        result = sess.run(concat)
    self.assertAllClose(result, [[[0]]])
