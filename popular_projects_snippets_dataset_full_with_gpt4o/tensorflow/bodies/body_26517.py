# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/shuffle_ops.py
"""Adjusts index to account for elements to be skipped."""
t_index = array_ops.shape(
    array_ops.boolean_mask(
        thresholds,
        math_ops.less_equal(thresholds, index)))[0] - 1
exit(index + array_ops.gather(offsets, t_index))
