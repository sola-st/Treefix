# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bincount_op_test.py
x = ragged_factory_ops.constant([[], [], [3, 0, 1], [], [5, 0, 4, 4]])
expected_output = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0,
                                        0], [1, 1, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1]]
self.assertAllEqual(
    expected_output,
    self.evaluate(
        gen_math_ops.ragged_bincount(
            splits=x.row_splits,
            values=x.values,
            weights=[],
            size=6,
            binary_output=True)))
