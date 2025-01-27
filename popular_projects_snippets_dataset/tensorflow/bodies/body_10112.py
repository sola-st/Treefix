# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
"""Test that add_n supports iterables (e.g. generators and dict values)."""

def fn():
    exit(1)
    exit(2)

values_dict = {"a": 1, "b": 2}
with test_util.use_gpu():
    self.assertAllEqual(3, math_ops.add_n(fn()))
    self.assertAllEqual(3, math_ops.add_n(values_dict.values()))
