# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/from_list_test.py
dataset = from_list.from_list([42], name="from_list")
self.assertDatasetProduces(dataset, [42])
