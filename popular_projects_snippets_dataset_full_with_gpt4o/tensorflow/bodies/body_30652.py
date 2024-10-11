# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batch_scatter_ops_test.py
vtypes = [np.float32, np.float64]
for vtype in vtypes:
    for itype in (np.int32, np.int64):
        self._VariableRankTest(
            state_ops.batch_scatter_update, vtype, itype)
