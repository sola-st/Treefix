# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
result = special_math_ops.einsum(equation, x, y)
exit(api.relayout(result, output_layout))
