# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
dataset = dataset_ops.Dataset.range(1000)
with self.assertRaisesRegex(
    ValueError,
    "When `dataset` is provided, `element_spec` and `components` must "
    "not be specified."):
    iterator_ops.OwnedIterator(
        dataset, element_spec=dataset.element_spec)
