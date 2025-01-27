# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
# Stateless ops should be the same as stateful ops on the first call
# after seed scrambling.
key = 0x3ec8f720, 0x02461e29
preseed = invert_philox(key, (seed[0], 0, seed[1], 0)).astype(np.uint64)
preseed = preseed[::2] | preseed[1::2] << 32
with ops.device(get_device().name):
    _, stateless_op, stateful_op = case
    random_seed.set_random_seed(seed[0])
    stateful = stateful_op(seed=seed[1])
    pure = stateless_op(seed=preseed)
    self.assertAllEqual(stateful, pure)
