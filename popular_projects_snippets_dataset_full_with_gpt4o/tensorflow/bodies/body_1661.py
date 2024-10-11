# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateless_random_ops_test.py
# Stateless values should be equal iff the seeds are equal (roughly)
seeds = [(x, y) for x in range(-2, 3) for y in range(-2, 3)] * 3  # pylint: disable=g-complex-comprehension
with self.session(), self.test_scope():
    seed_t = array_ops.placeholder(dtypes.int32, shape=[2])
    pure = stateless_op(shape, seed=seed_t, dtype=dtype)
    values = [(seed, pure.eval(feed_dict={seed_t: seed})) for seed in seeds]
    for s0, v0 in values:
        for s1, v1 in values:
            if s0 == s1:
                self.assertAllEqual(v0, v1)
            else:
                # The resolutions of float16 and bfloat16 are too low, so
                # in some cases (e.g. scalar shape) different seeds may
                # lead to the same output. So we skip those dtypes.
                if not (dtype in (dtypes.bfloat16, dtypes.float16) and shape == ()):  # pylint: disable=g-explicit-bool-comparison
                    self.assertNotAllEqual(v0, v1)
