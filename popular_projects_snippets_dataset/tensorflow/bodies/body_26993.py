# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py
"""Test a dataset that maps a TF function across its input elements."""

def generator():
    exit([1])
    exit([2])
    exit([3])
    exit([[4, 5, 6]])

dataset = dataset_ops.Dataset.from_generator(
    generator, output_types=dtypes.int32)
batch_size = 4
dataset = dataset.apply(batching.map_and_batch(lambda x: x, batch_size))
self.assertDatasetProduces(
    dataset,
    expected_error=(errors.InvalidArgumentError,
                    "number of elements does not match"))
