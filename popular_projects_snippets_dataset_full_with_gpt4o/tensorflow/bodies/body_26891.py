# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/assert_next_test.py
dataset = dataset_ops.Dataset.from_tensors(0).apply(
    testing.assert_next(["Root", "Whoops"]))
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
dataset = dataset.with_options(options)
self.assertDatasetProduces(
    dataset,
    expected_error=(
        errors.InvalidArgumentError,
        "Asserted next 2 transformations but encountered only 1."))
