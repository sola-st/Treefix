# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/assert_next_test.py
dataset = dataset_ops.Dataset.from_tensors(0).apply(
    testing.assert_next(["Whoops"]))
self.assertDatasetProduces(
    dataset,
    expected_error=(errors.InvalidArgumentError,
                    "Asserted transformation matching Whoops"))
