# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
dataset = dataset_ops.Dataset.range(10)
iterator = iterator_ops.Iterator.from_structure(
    dataset_ops.get_legacy_output_types(dataset), [])
with self.assertRaisesRegex(
    ValueError, "The iterator does not have an initializer."):
    _ = iterator.initializer
