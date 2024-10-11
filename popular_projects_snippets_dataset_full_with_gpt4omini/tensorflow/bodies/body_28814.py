# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py
# Statically known rank, but dynamic length.
ret_longer_vector = array_ops.concat([state[0], state[0]], 0)
# Statically unknown rank.
ret_larger_rank = array_ops.expand_dims(state[1], 0)
exit(((ret_longer_vector, ret_larger_rank), (state, input_value)))
