# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_partition_op_test.py
with self.session():
    data = constant_op.constant([0, 13, 2, 39, 4, 17], dtype=dtype)
    indices = constant_op.constant([0, 0, 2, 3, 2, 1])
    partitions = data_flow_ops.dynamic_partition(
        data, indices, num_partitions=4)
    partition_vals = self.evaluate(partitions)

self.assertEqual(4, len(partition_vals))
self.assertAllEqual([0, 13], partition_vals[0])
self.assertAllEqual([17], partition_vals[1])
self.assertAllEqual([2, 4], partition_vals[2])
self.assertAllEqual([39], partition_vals[3])
# Vector data input to DynamicPartition results in
# `num_partitions` vectors of unknown length.
self.assertEqual([None], partitions[0].get_shape().as_list())
self.assertEqual([None], partitions[1].get_shape().as_list())
self.assertEqual([None], partitions[2].get_shape().as_list())
self.assertEqual([None], partitions[3].get_shape().as_list())
