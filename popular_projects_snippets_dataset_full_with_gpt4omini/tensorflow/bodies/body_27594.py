# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/prefetch_with_slack_test.py
"""Should still work with a passthrough dataset after prefetch()."""
dataset = dataset_ops.Dataset.range(10)
dataset = dataset.prefetch(1)
dataset = dataset.map(lambda x: x + 1)
options = options_lib.Options()
options.experimental_slack = True
dataset = dataset.with_options(options)
self.assertDatasetProduces(dataset, range(1, 11))
