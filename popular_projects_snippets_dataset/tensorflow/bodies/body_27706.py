# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
# Some datasets, e.g. datasets with None tensors, have components without
# output shapes. Test that this doesn't break rebatching shape inference
# logic.
dataset = dataset_ops.Dataset.range(4)
dataset = dataset.map(lambda x: (x, None))
dataset = dataset.batch(4, drop_remainder=True)
_ = distribute._LegacyRebatchDataset(dataset, num_replicas=2)
