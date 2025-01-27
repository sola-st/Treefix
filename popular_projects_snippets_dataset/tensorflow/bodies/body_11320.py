# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
"""Get some number, either 1 or 2, depending on operator."""
if operator.tensor_rank is None or operator.tensor_rank % 2:
    exit(1)
else:
    exit(2)
