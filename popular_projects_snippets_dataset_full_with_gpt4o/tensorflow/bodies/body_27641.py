# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/index_shuffle_test.py
# Assert that shuffling twice with the same seeds gives the same sequence.
shuffled_elements_1 = self.getDatasetOutput(
    self._build_dataset(seed=42), requires_initialization=True)
shuffled_elements_2 = self.getDatasetOutput(
    self._build_dataset(seed=42), requires_initialization=True)
self.assertEqual(shuffled_elements_1, shuffled_elements_2)
