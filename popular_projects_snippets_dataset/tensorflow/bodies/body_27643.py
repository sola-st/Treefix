# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/index_shuffle_test.py
# Assert that shuffling twice with a different seed gives a different
# permutation of the same elements.
shuffled_elements_1 = self.getDatasetOutput(
    self._build_dataset(seed=42), requires_initialization=True)
shuffled_elements_2 = self.getDatasetOutput(
    self._build_dataset(seed=24), requires_initialization=True)
self.assertNotEqual(shuffled_elements_1, shuffled_elements_2)
self.assertAllEqual(
    sorted(shuffled_elements_1), sorted(shuffled_elements_2))
