# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/text_line_dataset_test.py
test_filenames = self._createFiles(2, 5, crlf=True)

repeat_dataset = readers.TextLineDataset(test_filenames, buffer_size=10)
expected_output = []
for j in range(2):
    expected_output.extend([self._lineText(j, i) for i in range(5)])
self.assertDatasetProduces(repeat_dataset, expected_output=expected_output)
