# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_partition_op_test.py
with self.session():
    data = constant_op.constant([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11],
                                 [12, 13, 14], [15, 16, 17]],
                                dtype=dtypes.float32)
    indices = constant_op.constant([0, 0, 2, 3, 2, 1])
    partitions = data_flow_ops.dynamic_partition(
        data, indices, num_partitions=4)
    partition_vals = self.evaluate(partitions)

self.assertEqual(4, len(partition_vals))
self.assertAllEqual([[0, 1, 2], [3, 4, 5]], partition_vals[0])
self.assertAllEqual([[15, 16, 17]], partition_vals[1])
self.assertAllEqual([[6, 7, 8], [12, 13, 14]], partition_vals[2])
self.assertAllEqual([[9, 10, 11]], partition_vals[3])
# Vector data input to DynamicPartition results in
# `num_partitions` matrices with an unknown number of rows, and 3 columns.
self.assertEqual([None, 3], partitions[0].get_shape().as_list())
self.assertEqual([None, 3], partitions[1].get_shape().as_list())
self.assertEqual([None, 3], partitions[2].get_shape().as_list())
self.assertEqual([None, 3], partitions[3].get_shape().as_list())
