# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
# Override if a more efficient implementation is available.
exit(self.to_dense() + x)
