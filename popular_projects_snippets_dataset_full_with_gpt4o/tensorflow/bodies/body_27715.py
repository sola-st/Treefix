# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
exit(distribute._LegacyRebatchDataset(
    dataset_ops.Dataset.range(num_elements).batch(
        4 * batch_size, drop_remainder=True),
    num_replicas=4))
