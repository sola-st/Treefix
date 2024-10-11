# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Assert ndarray data type is equal to expected.

    Args:
      target: The numpy `ndarray`, or anything that can be converted into a
        numpy `ndarray` (including Tensor).
      expected_dtype: Expected data type.
    """
target = self._GetNdArray(target)
if not isinstance(target, list):
    arrays = [target]
for arr in arrays:
    self.assertEqual(arr.dtype, expected_dtype)
