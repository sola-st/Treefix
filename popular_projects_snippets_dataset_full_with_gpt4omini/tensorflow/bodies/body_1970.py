# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/categorical_op_test.py
# Stateless values should be equal iff the seeds are equal (roughly)
num_samples = 10
with self.session(), self.test_scope():
    seed_t = array_ops.placeholder(dtypes.int32, shape=[2])
    seeds = [(x, y) for x in range(5) for y in range(5)] * 3
    for logits in ([[0.1, 0.25, 0.5, 0.15]], [[0.5, 0.5], [0.8, 0.2],
                                              [0.25, 0.75]]):
        pure = stateless_random_ops.stateless_multinomial(
            logits, num_samples, seed=seed_t)
        values = [(seed, pure.eval(feed_dict={seed_t: seed})) for seed in seeds]
        for s0, v0 in values:
            for s1, v1 in values:
                self.assertEqual(s0 == s1, np.all(v0 == v1))
