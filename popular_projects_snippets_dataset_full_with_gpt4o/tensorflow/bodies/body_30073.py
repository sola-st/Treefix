# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
make_mask = lambda shape: np.zeros(shape, dtype=bool)
for ndims_mask in range(1, 4):
    for ndims_arr in range(ndims_mask, ndims_mask + 3):
        for _ in range(3):
            with self.subTest(ndims_mask=ndims_mask, ndims_arr=ndims_arr, _=_):
                arr_shape = np.random.randint(1, 5, size=ndims_arr)
                self.CheckVersusNumpy(ndims_mask, arr_shape, make_mask=make_mask)
