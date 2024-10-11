# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/substr_op_test.py
test_string = [[b"ten", b"eleven", b"twelve"],
               [b"thirteen", b"fourteen", b"fifteen"],
               [b"sixteen", b"seventeen", b"eighteen"]]
position = np.array([1, 2, -3, 4], dtype)
length = np.array([1, 2, 3, 4], dtype)
with self.assertRaises(ValueError):
    string_ops.substr(test_string, position, length, unit=unit)
