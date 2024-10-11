# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
dataset = dataset_ops.Dataset.from_tensors(42)
options = options_lib.Options()
dataset = dataset.with_options(options, name="options")
self.assertDatasetProduces(dataset, [42])
