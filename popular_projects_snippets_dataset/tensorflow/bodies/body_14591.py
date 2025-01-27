# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
# List of 2-tuples of fill value and shape.
data = [
    (5, ()),
    (5, (7,)),
    (5., (7,)),
    ([5, 8], (2,)),
    ([5, 8], (3, 2)),
    ([[5], [8]], (2, 3)),
    ([[5], [8]], (3, 2, 5)),
    ([[5.], [8.]], (3, 2, 5)),
    ([[3, 4], [5, 6], [7, 8]], (3, 3, 2)),
]
for f, s in data:
    for fn1, fn2 in itertools.product(self.array_transforms,
                                      self.shape_transforms):
        fill_value = fn1(f)
        shape = fn2(s)
        self.match(
            np_array_ops.full(shape, fill_value), np.full(shape, fill_value))
        for dtype in self.all_types:
            self.match(
                np_array_ops.full(shape, fill_value, dtype=dtype),
                np.full(shape, fill_value, dtype=dtype))
