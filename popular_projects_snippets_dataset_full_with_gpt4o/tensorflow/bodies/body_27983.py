# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/random_test.py
expect_determinism = (global_seed is not None) or (local_seed is not None)

random_seed.set_random_seed(global_seed)
ds = dataset_ops.Dataset.random(seed=local_seed).take(10)

output_1 = self.getDatasetOutput(ds, requires_initialization=True)
ds = self.graphRoundTrip(ds)
output_2 = self.getDatasetOutput(ds, requires_initialization=True)

if expect_determinism:
    self.assertEqual(output_1, output_2)
else:
    # Technically not guaranteed since the two randomly-chosen int64 seeds
    # could match, but that is sufficiently unlikely (1/2^128 with perfect
    # random number generation).
    self.assertNotEqual(output_1, output_2)
