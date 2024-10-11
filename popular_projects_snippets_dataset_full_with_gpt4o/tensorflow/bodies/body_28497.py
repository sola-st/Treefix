# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
# TensorFlow unit tests set the global graph seed. We unset it here so that
# we can control determinism via the `seed` parameter.
random_seed.set_random_seed(None)
dataset = dataset_ops.Dataset.range(10).shuffle(
    10, seed=seed, reshuffle_each_iteration=reshuffle)

first_epoch = self.getDatasetOutput(dataset)
second_epoch = self.getDatasetOutput(dataset)

self.assertEqual(first_epoch == second_epoch, not reshuffle)
