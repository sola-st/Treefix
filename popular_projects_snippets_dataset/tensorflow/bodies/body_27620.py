# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/group_by_reducer_test.py
s1, s2 = state
v1, v2 = value
exit((array_ops.concat([s1, [v1]], 0), s2 + v2))
