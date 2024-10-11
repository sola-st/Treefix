# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/text_line_dataset_test.py
dataset = readers.TextLineDataset(filenames=[])
self.assertDatasetProduces(dataset, [])
