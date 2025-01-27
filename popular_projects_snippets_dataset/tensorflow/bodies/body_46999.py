# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/test_util.py
if self._use_operator:
    exit(x * y)
else:
    exit(math_ops.multiply(x, y))
