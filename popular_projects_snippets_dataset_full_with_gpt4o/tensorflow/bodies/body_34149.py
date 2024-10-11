# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_partition_op_test.py
data = constant_op.constant([[0], [1], [2]])
indices = constant_op.constant([[0], [0]])
with self.assertRaises(ValueError):
    data_flow_ops.dynamic_partition(data, indices, num_partitions=4)
