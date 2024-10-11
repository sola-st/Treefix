# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops_test.py
x = ragged_factory_ops.constant([[], [], [3, 0, 1], [], [5, 0, 4, 4]])
weights = ragged_factory_ops.constant([[], [], [.1, .2, .3], [],
                                       [.2, .5, .6, .3]])
# pyformat: disable
expected_output = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [.2, .3, 0, .1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [.5, 0, 0, 0, .9, .2]]
# pyformat: enable
self.assertAllClose(
    expected_output,
    self.evaluate(bincount_ops.bincount(arr=x, weights=weights, axis=-1)))
