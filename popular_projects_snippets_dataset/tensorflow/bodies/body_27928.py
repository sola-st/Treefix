# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/text_line_dataset_test.py
test_filenames = self._createFiles(10, 10)
files = dataset_ops.Dataset.from_tensor_slices(test_filenames).repeat(10)
expected_output = []
for j in range(10):
    expected_output.extend(self._lineText(j, i) for i in range(10))
dataset = readers.TextLineDataset(files, num_parallel_reads=4)
self.assertDatasetProduces(
    dataset, expected_output=expected_output * 10, assert_items_equal=True)
