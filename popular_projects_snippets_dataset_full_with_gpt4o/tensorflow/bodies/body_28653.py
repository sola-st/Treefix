# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
self.assertEqual(
    nest.flatten(input_datasets),
    dataset_fn(input_datasets)._inputs())
