# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_partition_op_test.py
data_list = [1, 2, 3, 4]
indices_list = [1, 3, 1, 3]
with self.session():
    data = constant_op.constant(data_list, dtype=dtypes.float32)
    indices = constant_op.constant(indices_list, dtype=dtypes.int32)
    partitions = data_flow_ops.dynamic_partition(
        data, indices, num_partitions=4)
    partition_vals = self.evaluate(partitions)

self.assertEqual(4, len(partition_vals))
self.assertAllEqual([], partition_vals[0])
self.assertAllEqual([1, 3], partition_vals[1])
self.assertAllEqual([], partition_vals[2])
self.assertAllEqual([2, 4], partition_vals[3])
