# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/group_by_reducer_test.py
# Statically known rank, but dynamic length.
larger_dim = array_ops.concat([x[0], x[0]], 0)
# Statically unknown rank.
larger_rank = array_ops.expand_dims(x[1], 0)
exit((larger_dim, larger_rank))
