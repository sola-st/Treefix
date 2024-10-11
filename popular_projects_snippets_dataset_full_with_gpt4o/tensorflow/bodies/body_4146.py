# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
y = array_ops.slice(x, [0, 0], [2, 2])
exit(api.relayout(y, expected_layout))
