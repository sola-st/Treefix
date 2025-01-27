# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
# Test case for GitHub issue 46899.
with self.session():
    with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
        v = math_ops.range(start=-1e+38, limit=1)
        self.evaluate(v)
