# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
mystr = "hello"
with self.assertRaisesRegex(TypeError, "proper"):
    check_ops.assert_proper_iterable(mystr)
