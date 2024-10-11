# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/prefetch_with_slack_test.py
"""The rewrite should not fail if there is no prefetch() in the pipeline."""
dataset = dataset_ops.Dataset.range(10)
options = options_lib.Options()
options.experimental_slack = True
dataset = dataset.with_options(options)
self.assertDatasetProduces(dataset, range(10))
