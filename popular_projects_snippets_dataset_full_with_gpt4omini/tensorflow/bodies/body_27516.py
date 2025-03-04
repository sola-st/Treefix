# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/assert_prev_test.py
dataset = dataset_ops.Dataset.from_tensors(0).apply(
    testing.assert_prev([("TensorDataset", {}), ("Whoops", {})]))
self.assertDatasetProduces(
    dataset,
    expected_error=(
        errors.InvalidArgumentError,
        "Asserted previous 2 transformations but encountered only 1."))
