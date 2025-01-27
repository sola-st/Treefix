# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bincount_op_test.py
x = ragged_factory_ops.constant([[], [], [3, 0, 1], [], [5, 0, 4, 4]])
weights = ragged_factory_ops.constant([[], [], [.1, .2, .3], [],
                                       [.2, .5, .6, .3]])
expected_output = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                   [.2, .3, 0, .1, 0, 0], [0, 0, 0, 0, 0, 0],
                   [.5, 0, 0, 0, .9, .2]]
self.assertAllClose(
    expected_output,
    self.evaluate(
        gen_math_ops.ragged_bincount(
            splits=x.row_splits,
            values=x.values,
            weights=weights.values,
            size=6)))
