# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
for vtype in (np.int32, np.float16, np.float32, np.float64, np.complex64,
              np.complex128, dtypes.bfloat16.as_numpy_dtype):
    for itype in (np.int32, np.int64):
        self._VariableRankTest(np_scatter, tf_scatter, vtype, itype)
