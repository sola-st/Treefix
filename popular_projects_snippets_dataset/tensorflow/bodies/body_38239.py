# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bincount_op_test.py
# unsorted_segment_sum will only report InvalidArgumentError on CPU
with self.cached_session(), ops.device("/CPU:0"):
    with self.assertRaises(errors.InvalidArgumentError):
        self.evaluate(bincount_ops.bincount([1, 2, 3, -1, 6, 8]))
