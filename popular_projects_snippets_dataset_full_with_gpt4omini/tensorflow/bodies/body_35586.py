# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
# Stateless values should be equal iff the seeds are equal (roughly)
seeds = [(x, y) for x in range(5) for y in range(5)] * 3  # pylint: disable=g-complex-comprehension
with self.test_session(), ops.device(get_device().name):
    _, stateless_op, _ = case
    if context.executing_eagerly():
        values = [
            (seed, stateless_op(seed=constant_op.constant(seed, seed_type)))
            for seed in seeds]
    else:
        # Have this branch because the above branch is too slow in graph
        # mode
        seed_t = array_ops.placeholder(seed_type, shape=[2])
        pure = stateless_op(seed=seed_t)
        values = [
            (seed, pure.eval(feed_dict={seed_t: seed})) for seed in seeds
        ]
    for s0, v0 in values:
        for s1, v1 in values:
            if dtypes.as_dtype(v0.dtype) != dtypes.bfloat16:
                self.assertEqual(s0 == s1, np.all(v0 == v1))
            elif s0 == s1:
                # Skip the s0 != s1 case because v0 and v1 can be either equal or
                # unequal in that case due to bfloat16's low precision
                self.assertAllEqual(v0, v1)
