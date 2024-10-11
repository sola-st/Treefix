# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/index_shuffle_test.py
# Assert that the shuffled dataset has the same elements as the
# "ground truth".
unshuffled_elements = np.arange(50)
shuffled_elements_1 = self.getDatasetOutput(
    self._build_dataset(), requires_initialization=True)
shuffled_elements_2 = self.getDatasetOutput(
    self._build_dataset(), requires_initialization=True)
self.assertAllEqual(
    sorted(unshuffled_elements), sorted(shuffled_elements_1))
self.assertAllEqual(
    sorted(unshuffled_elements), sorted(shuffled_elements_2))
self.assertNotEqual(shuffled_elements_1, shuffled_elements_2)
