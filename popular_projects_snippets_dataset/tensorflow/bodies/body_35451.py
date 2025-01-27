# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/candidate_sampler_ops_test.py
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "out of range"):
    self.evaluate(
        candidate_sampling_ops.log_uniform_candidate_sampler(
            true_classes=[[0, 10]],
            num_true=2,
            num_sampled=1000,
            unique=False,
            range_max=2))

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "out of range"):
    self.evaluate(
        candidate_sampling_ops.log_uniform_candidate_sampler(
            true_classes=[[0, -10]],
            num_true=2,
            num_sampled=1000,
            unique=False,
            range_max=2))
