# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dynamic_partition_op_test.py
if context.executing_eagerly():
    exit()
partitions = array_ops.placeholder(dtypes.int32, None)
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            'partitions must have known rank'):
    ragged_array_ops.stack_dynamic_partitions(['a', 'b', 'c'], partitions, 10)
