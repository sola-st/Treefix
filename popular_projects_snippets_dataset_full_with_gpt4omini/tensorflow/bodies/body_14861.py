# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py

def run_test(arr, *args, **kwargs):
    check_dtype = kwargs.pop('check_dtype', True)
    for fn in self.array_transforms:
        arr = fn(arr)
        self.match(
            np_math_ops.clip(arr, *args, **kwargs),
            np.clip(arr, *args, **kwargs),
            check_dtype=check_dtype)

    # NumPy exhibits weird typing behavior when a/a_min/a_max are scalars v/s
    # lists, e.g.,
    #
    # np.clip(np.array(0, dtype=np.int32), -5, 5).dtype == np.int64
    # np.clip(np.array([0], dtype=np.int32), -5, 5).dtype == np.int32
    # np.clip(np.array([0], dtype=np.int32), [-5], [5]).dtype == np.int64
    #
    # So we skip matching type. In tf-numpy the type of the output array is
    # always the same as the input array.
run_test(0, -1, 5, check_dtype=False)
run_test(-1, -1, 5, check_dtype=False)
run_test(5, -1, 5, check_dtype=False)
run_test(-10, -1, 5, check_dtype=False)
run_test(10, -1, 5, check_dtype=False)
run_test(10, None, 5, check_dtype=False)
run_test(10, -1, None, check_dtype=False)
run_test([0, 20, -5, 4], -1, 5, check_dtype=False)
run_test([0, 20, -5, 4], None, 5, check_dtype=False)
run_test([0, 20, -5, 4], -1, None, check_dtype=False)
run_test([0.5, 20.2, -5.7, 4.4], -1.5, 5.1, check_dtype=False)

run_test([0, 20, -5, 4], [-5, 0, -5, 0], [0, 5, 0, 5], check_dtype=False)
run_test([[1, 2, 3], [4, 5, 6]], [2, 0, 2], 5, check_dtype=False)
run_test([[1, 2, 3], [4, 5, 6]], 0, [5, 3, 1], check_dtype=False)
