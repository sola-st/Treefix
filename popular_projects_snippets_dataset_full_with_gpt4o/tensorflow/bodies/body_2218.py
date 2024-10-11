# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scatter_nd_op_test.py
for vtype in self.numeric_types:
    for itype in set([np.int32, np.int64]).intersection(set(self.int_types)):
        self._VariableRankTest(np_scatter, tf_scatter, vtype, itype)
