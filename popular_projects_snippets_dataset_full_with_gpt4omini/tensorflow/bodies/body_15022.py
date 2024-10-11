# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dynamic_partition_op_test.py
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            error):
    ragged_array_ops.stack_dynamic_partitions(data, partitions,
                                              num_partitions)
