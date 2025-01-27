# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/partitioned_variables_test.py
partitioner = partitioned_variables.variable_axis_size_partitioner(
    axis=axis, max_shard_bytes=max_shard_bytes, max_shards=max_shards)

with variable_scope.variable_scope("root", partitioner=partitioner):
    v0 = variable_scope.get_variable(
        name, dtype=dtypes.float32, shape=(4, 8, 16, 32))
    v0_list = v0._get_variable_list()
    v0_part = v0._get_partitions()
    self.assertEqual(len(v0_list), expected_axis_shards)
    self.assertAllEqual(v0_part, expected_partitions)
