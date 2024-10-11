# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sharding_util_ops_test.py
for dtype in self.numeric_types:
    with self.session() as sess, self.device_scope():
        split = graph_fn(
            sess,
            input_value=[
                [0, 1, 2, 3],
                [4, 5, 6, 7],
                [8, 9, 10, 11],
                [12, 13, 14, 15],
            ],
            input_dtype=dtype,
            num_outputs=4,
            num_splits=[2, 2])
        results = sess.run(split)
    self.assertLen(results, 4)
    self.assertAllClose(results[0], [[0, 1], [4, 5]])
    self.assertAllClose(results[1], [[2, 3], [6, 7]])
    self.assertAllClose(results[2], [[8, 9], [12, 13]])
    self.assertAllClose(results[3], [[10, 11], [14, 15]])
