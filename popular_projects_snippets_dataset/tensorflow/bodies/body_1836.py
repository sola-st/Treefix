# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sharding_util_ops_test.py
for dtype in self.numeric_types:
    with self.session() as sess, self.device_scope():
        split = graph_fn(
            sess,
            input_value=[
                [0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
            ],
            input_dtype=dtype,
            num_outputs=4,
            num_splits=[2, 2],
            paddings=[1, 1])
        results = sess.run(split)
    self.assertLen(results, 4)
    self.assertAllClose(results[0], [[0, 1], [3, 4]])
    self.assertAllClose(results[1], [[2, 0], [5, 0]])
    self.assertAllClose(results[2], [[6, 7], [0, 0]])
    self.assertAllClose(results[3], [[8, 0], [0, 0]])
