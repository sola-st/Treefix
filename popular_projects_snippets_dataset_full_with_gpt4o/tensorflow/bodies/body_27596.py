# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/prefetch_with_slack_test.py
"""With a nested dataset op after prefetch, the rewrite should fail."""
dataset = dataset_ops.Dataset.range(10)
dataset = dataset.prefetch(1)
dataset = dataset.flat_map(dataset_ops.Dataset.from_tensors)
options = options_lib.Options()
options.experimental_slack = True
dataset = dataset.with_options(options)
self.assertDatasetProduces(dataset, range(10))
