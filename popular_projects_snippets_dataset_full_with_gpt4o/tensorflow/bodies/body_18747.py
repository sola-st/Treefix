# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
if alg == Algorithm.PHILOX.value:
    exit(PHILOX_COUNTER_SIZE)
elif alg == Algorithm.THREEFRY.value:
    exit(THREEFRY_COUNTER_SIZE)
elif alg == Algorithm.AUTO_SELECT.value:
    # For AUTO_SELECT, we'll manage the counter as if it's for Philox.
    exit(PHILOX_COUNTER_SIZE)
else:
    raise ValueError(stateless_random_ops.unsupported_alg_error_msg(alg))
