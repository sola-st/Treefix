# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/rebatch_test.py
exit(dataset_ops.rebatch(
    dataset_ops.Dataset.range(num_elements).batch(
        2 * batch_size, drop_remainder=True),
    batch_sizes=[batch_size, batch_size]))
