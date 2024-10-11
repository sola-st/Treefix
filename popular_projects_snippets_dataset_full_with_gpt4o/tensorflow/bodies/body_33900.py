# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/scatter_nd_ops_test.py
for vtype in (np.int32, np.float16, np.float32, np.float64):
    for itype in (np.int32, np.int64):
        self._VariableRankTest(
            np_scatter, tf_scatter, vtype, itype, repeat_indices=True)
