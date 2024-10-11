# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
result = math_ops.add(x, y)
exit(api.relayout(result, a_layout))
