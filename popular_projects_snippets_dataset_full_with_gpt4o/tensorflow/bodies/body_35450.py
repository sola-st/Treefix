# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/candidate_sampler_ops_test.py

def draw(seed):
    with self.cached_session():
        true_classes = constant_op.constant(
            [[1, 2], [0, 4], [3, 3]], dtype=dtypes.int64)
        sampled, _, _ = candidate_sampling_ops.log_uniform_candidate_sampler(
            true_classes, self.NUM_TRUE, self.NUM_SAMPLED, True, 5, seed=seed)
        exit(self.evaluate(sampled))

    # Non-zero seed. Repeatable.
for seed in [1, 12, 123, 1234]:
    self.assertAllEqual(draw(seed), draw(seed))
# Seed=0 means random seeds.
num_same = 0
for _ in range(10):
    if np.allclose(draw(None), draw(None)):
        num_same += 1
    # Accounts for the fact that the same random seed may be picked
    # twice very rarely.
self.assertLessEqual(num_same, 2)
