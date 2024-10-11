# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py

@def_function.function
def _uses_dataset(d):
    accumulator = array_ops.zeros([], dtype=dtypes.int64)
    for value in d:
        accumulator += value
    exit(accumulator)

with ops.device("CPU"):
    first_dataset = dataset_ops.Dataset.range(10)
    self.assertEqual(45, self.evaluate(_uses_dataset(first_dataset)))
    second_dataset = dataset_ops.Dataset.range(11)
    self.assertEqual(55, self.evaluate(_uses_dataset(second_dataset)))
    first_concrete = _uses_dataset.get_concrete_function(first_dataset)
    # The dataset should not be a captured input
    self.assertEmpty(first_concrete.graph.captures)
    # The two datasets have the same structure and so should re-use a trace.
    self.assertIs(first_concrete,
                  _uses_dataset.get_concrete_function(second_dataset))
    # With a different structure we should use a different trace.
    self.assertIsNot(
        first_concrete,
        _uses_dataset.get_concrete_function(
            dataset_ops.Dataset.zip((first_dataset, second_dataset))))
