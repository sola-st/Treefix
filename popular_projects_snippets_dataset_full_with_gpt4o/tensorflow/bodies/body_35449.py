# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/candidate_sampler_ops_test.py
with self.cached_session():
    true_classes = constant_op.constant(
        [[1, 2], [0, 4], [3, 3]], dtype=dtypes.int64)
    sampled, _, _ = candidate_sampling_ops.log_uniform_candidate_sampler(
        true_classes, self.NUM_TRUE, self.NUM_SAMPLED, True, 5, seed=seed)
    exit(self.evaluate(sampled))
