# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_range_op_test.py
expected = [[0.0, 0.4, 0.8, 1.2, 1.6, 2.0, 2.4, 2.8, 3.2, 3.6], [3.0],
            [5.0, 7.2, 9.4, 11.6, 13.8]]
actual = ragged_math_ops.range([0.0, 3.0, 5.0], [3.9, 4.0, 15.0],
                               [0.4, 1.5, 2.2])
self.assertAllClose(actual, expected)
