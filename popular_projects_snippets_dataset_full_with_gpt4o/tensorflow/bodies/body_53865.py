# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Assert element values are all less than a target value.

    Args:
      a: The numpy `ndarray`, or anything that can be converted into a numpy
        `ndarray` (including Tensor).
      comparison_target: The target value of comparison.
    """
(a, comparison_target) = self.evaluate_if_both_tensors(a, comparison_target)
a = self._GetNdArray(a)
self.assertLess(np.max(a), comparison_target)
