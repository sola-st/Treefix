# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Assert that elements of a Tensor are all in a given closed set.

    Args:
      target: The numpy `ndarray`, or anything that can be converted into a
        numpy `ndarray` (including Tensor).
      expected_set: (`list`, `tuple` or `set`) The closed set that the elements
        of the value of `target` are expected to fall into.

    Raises:
      AssertionError:
        if any of the elements do not fall into `expected_set`.
    """
target = self._GetNdArray(target)

# Elements in target that are not in expected_set.
diff = np.setdiff1d(target.flatten(), list(expected_set))
if np.size(diff):
    raise AssertionError("%d unique element(s) are not in the set %s: %s" %
                         (np.size(diff), expected_set, diff))
