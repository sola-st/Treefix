# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/partitioned_variables_test.py
with self.cached_session():
    partitioner = partitioned_variables.fixed_size_partitioner(5, axis=0)
    with variable_scope.variable_scope("root", partitioner=partitioner):
        v0 = variable_scope.get_variable(
            "v0", dtype=dtypes.float32, shape=(10, 10))
        v0_list = v0._get_variable_list()
        v0_part = v0._get_partitions()
        self.assertEqual(len(v0_list), 5)
        self.assertAllEqual(v0_part, (5, 1))
