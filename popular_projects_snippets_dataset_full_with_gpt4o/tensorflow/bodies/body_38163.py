# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
if dtype != dtypes_lib.bfloat16.as_numpy_dtype:
    fi = np.finfo(dtype)
    data = np.array([
        0, -1, 1, fi.resolution, -fi.resolution, fi.min, fi.max, -np.inf,
        np.inf, np.nan
    ]).astype(dtype)
else:
    # np.finfo does not support bfloat16
    data = np.array([
        0, -1, 1, 0.01, -0.01, -3.3895e+38, 3.3895e+38, -np.inf, np.inf,
        np.nan
    ]).astype(dtype)
self._compare(data, use_gpu=False)
self._compare(data, use_gpu=True)
