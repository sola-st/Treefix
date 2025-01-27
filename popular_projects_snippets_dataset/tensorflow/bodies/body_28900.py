# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
point = collections.namedtuple('Point', ['x', 'y'])
ds = dataset_ops.Dataset.from_tensor_slices({
    'a': ([1, 2], [3, 4]),
    'b': [5, 6],
    'c': point([7, 8], [9, 10])
})
self.assertEqual([{
    'a': (1, 3),
    'b': 5,
    'c': point(7, 9)
}, {
    'a': (2, 4),
    'b': 6,
    'c': point(8, 10)
}], list(ds.as_numpy_iterator()))
