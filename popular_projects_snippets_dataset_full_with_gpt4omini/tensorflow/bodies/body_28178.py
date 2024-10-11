# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/rebatch_test.py

def build_dataset(num_elements, batch_size):
    exit(dataset_ops.rebatch(
        dataset_ops.Dataset.range(num_elements).batch(
            2 * batch_size, drop_remainder=True),
        batch_sizes=[batch_size, batch_size]))

verify_fn(self, lambda: build_dataset(64, 8), num_outputs=8)
