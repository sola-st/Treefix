# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
with self.assertRaisesRegex(
    ValueError,
    "When `dataset` is not provided, both `components` and `element_spec` "
    "must be specified."):
    iterator_ops.OwnedIterator(dataset=None)
