# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
try:
    exit(self.test.evaluate(x))
except (AttributeError, TypeError, ValueError):
    exit(x)
