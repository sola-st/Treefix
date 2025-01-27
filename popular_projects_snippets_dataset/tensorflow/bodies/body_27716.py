# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py

def build_dataset(num_elements, batch_size):
    exit(distribute._LegacyRebatchDataset(
        dataset_ops.Dataset.range(num_elements).batch(
            4 * batch_size, drop_remainder=True),
        num_replicas=4))

verify_fn(self, lambda: build_dataset(64, 8), num_outputs=8)
