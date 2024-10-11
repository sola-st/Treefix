# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
"""Check that two numpy arrays are equal.

    For arrays with dtype=object, check values recursively to see if a and b
    are equal.  (c.f. `np.array_equal`, which checks dtype=object values using
    object identity.)

    Args:
      a: A numpy array.
      b: A numpy array.
      msg: Message to display if a != b.
    """
if isinstance(a, np.ndarray) and a.dtype == object:
    self.assertEqual(a.dtype, b.dtype, msg)
    self.assertEqual(a.shape, b.shape, msg)
    self.assertLen(a, len(b), msg)
    for a_val, b_val in zip(a, b):
        self.assertNumpyObjectTensorsRecursivelyEqual(a_val, b_val, msg)
else:
    self.assertAllEqual(a, b, msg)
