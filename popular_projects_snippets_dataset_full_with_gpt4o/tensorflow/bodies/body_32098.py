# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/substr_op_test.py
# Test case for GitHub issue 46900.
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    x = string_ops.substr(b"abc", len=1, pos=[1, -1])
    self.evaluate(x)

with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    x = string_ops.substr(b"abc", len=1, pos=[1, 2])
    self.evaluate(x)
