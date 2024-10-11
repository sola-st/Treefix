# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_partition_op_test.py
data_list = []
indices_list = []
with self.session():
    data = constant_op.constant(data_list, dtype=dtypes.float32)
    indices = constant_op.constant(indices_list, dtype=dtypes.int32)
    partitions = data_flow_ops.dynamic_partition(
        data, indices, num_partitions=2)
    partition_vals = self.evaluate(partitions)

self.assertEqual(2, len(partition_vals))
self.assertAllEqual([], partition_vals[0])
self.assertAllEqual([], partition_vals[1])
