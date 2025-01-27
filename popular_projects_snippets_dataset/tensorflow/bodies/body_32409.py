# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
array = np.array([1, 2, 3])
with self.assertRaisesRegex(TypeError, "proper"):
    check_ops.assert_proper_iterable(array)
