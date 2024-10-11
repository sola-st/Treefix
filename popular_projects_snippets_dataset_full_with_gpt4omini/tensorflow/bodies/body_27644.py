# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/index_shuffle_test.py
# Assert that `reshuffle_each_iteration` controls whether data is shuffled
# differently across different epochs.
dataset = self._build_dataset(
    seed=42, reshuffle_each_iteration=reshuffle_each_iteration)
shuffled_elements_1 = self.getDatasetOutput(dataset)
shuffled_elements_2 = self.getDatasetOutput(dataset)
if reshuffle_each_iteration:
    self.assertNotEqual(shuffled_elements_1, shuffled_elements_2)
    self.assertAllEqual(
        sorted(shuffled_elements_1), sorted(shuffled_elements_2))
else:
    self.assertAllEqual(shuffled_elements_1, shuffled_elements_2)
