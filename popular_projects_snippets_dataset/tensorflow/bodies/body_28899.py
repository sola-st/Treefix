# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
ds = dataset_ops.Dataset.from_tensors([1, 2, 3])
arr = next(ds.as_numpy_iterator())
with self.assertRaisesRegex(ValueError,
                            'assignment destination is read-only'):
    arr[0] = 0
