# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/text_line_dataset_test.py
files = self._createFiles(1, 5)
files = [pathlib.Path(f) for f in files]

expected_output = [self._lineText(0, i) for i in range(5)]
ds = readers.TextLineDataset(files)
self.assertDatasetProduces(
    ds, expected_output=expected_output, assert_items_equal=True)
