# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/text_line_dataset_test.py
dataset = readers.TextLineDataset(filenames=["File not exist"])
with self.assertRaisesRegex(errors.NotFoundError,
                            "No such file or directory"):
    self.getDatasetOutput(dataset)
