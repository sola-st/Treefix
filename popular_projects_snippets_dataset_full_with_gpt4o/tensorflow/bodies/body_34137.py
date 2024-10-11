# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_partition_op_test.py
data_list = [1 + 2j, 3 + 4j, 5 + 6j, 7 + 8j]
indices_list = [1, 0, 1, 0]
with self.session():
    data = constant_op.constant(data_list, dtype=dtypes.complex64)
    indices = constant_op.constant(indices_list, dtype=dtypes.int32)
    partitions = data_flow_ops.dynamic_partition(
        data, indices, num_partitions=2)
    partition_vals = self.evaluate(partitions)

self.assertEqual(2, len(partition_vals))
self.assertAllEqual([3 + 4j, 7 + 8j], partition_vals[0])
self.assertAllEqual([1 + 2j, 5 + 6j], partition_vals[1])
