# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dynamic_partition_op_test.py
data = ragged_factory_ops.constant(data)
partitions = ragged_factory_ops.constant(partitions, dtype=dtypes.int64)
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            error):
    self.evaluate(
        ragged_array_ops.stack_dynamic_partitions(data, partitions,
                                                  num_partitions))
