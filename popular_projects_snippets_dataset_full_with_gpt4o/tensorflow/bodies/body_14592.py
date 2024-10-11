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
]
zeros_builders = [np_array_ops.zeros, np.zeros]
for f, s in data:
    for fn1, fn2, arr_dtype in itertools.product(self.array_transforms,
                                                 zeros_builders,
                                                 self.all_types):
        fill_value = fn1(f)
        arr = fn2(s, arr_dtype)
        self.match(
            np_array_ops.full_like(arr, fill_value),
            np.full_like(arr, fill_value))
        for dtype in self.all_types:
            self.match(
                np_array_ops.full_like(arr, fill_value, dtype=dtype),
                np.full_like(arr, fill_value, dtype=dtype))
