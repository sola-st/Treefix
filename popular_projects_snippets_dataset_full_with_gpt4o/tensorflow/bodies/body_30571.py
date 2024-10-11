# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
# Test case for GitHub issue 46913.
with self.session():
    with self.assertRaises(errors_impl.ResourceExhaustedError):
        v = math_ops.range(0, 9223372036854775807)
        self.evaluate(v)
