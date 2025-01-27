# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_ops_test.py
vtypes = [np.float32, np.float64, dtypes.bfloat16.as_numpy_dtype]
if tf_scatter != state_ops.scatter_div:
    vtypes.append(np.int32)
    # float16 is numerically unstable for div
    vtypes.append(np.float16)

for vtype in vtypes:
    for itype in (np.int32, np.int64):
        self._VariableRankTest(tf_scatter, vtype, itype, repeat_indices,
                               updates_are_scalar)
