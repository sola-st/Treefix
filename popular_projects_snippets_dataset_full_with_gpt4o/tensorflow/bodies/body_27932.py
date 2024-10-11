# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/text_line_dataset_test.py
files = self._createFiles(1, 5)
expected_output = [self._lineText(0, i) for i in range(5)]
ds = readers.TextLineDataset(files, name="text_line_dataset")
self.assertDatasetProduces(
    ds, expected_output=expected_output, assert_items_equal=True)
