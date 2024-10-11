# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/partitioned_variables_test.py
with self.cached_session():
    partitioner = partitioned_variables.fixed_size_partitioner(4, axis=0)
    with variable_scope.variable_scope("root", partitioner=partitioner):
        v0 = variable_scope.get_variable("v0", dtype=dtypes.int64, shape=[20])
        v0_list = v0._get_variable_list()
        self.assertEqual(len(v0_list), 4)
