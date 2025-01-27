# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/partitioned_variables_test.py
partitioner = partitioned_variables.min_max_variable_partitioner(
    max_partitions=max_partitions, axis=axis, min_slice_size=min_slice_size)
with variable_scope.variable_scope("root", partitioner=partitioner):
    v0 = variable_scope.get_variable(
        var_name, dtype=dtypes.float32, shape=var_shape)
    v0_list = v0._get_variable_list()
    v0_part = v0._get_partitions()
    self.assertEqual(len(v0_list), expected_axis_shards)
    self.assertAllEqual(v0_part, expected_partitions)
