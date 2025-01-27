# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
ndims_mask = 1
for arr_shape in [(1, 1), (2, 2), (2, 5)]:
    with self.subTest(arr_shape=arr_shape):
        self.CheckVersusNumpy(ndims_mask, arr_shape, axis=1)
