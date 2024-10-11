# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops_test.py
x = ragged_factory_ops.constant([[], [], [3, 0, 1], [], [5, 0, 4, 4]],
                                dtype)
# pyformat: disable
expected_output = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 2, 1]]
# pyformat: enable
self.assertAllEqual(expected_output,
                    self.evaluate(bincount_ops.bincount(arr=x, axis=-1)))
