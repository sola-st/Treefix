# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_partition_op_test.py
data_list = [10, 13, 12, 11]
with self.session():
    data = constant_op.constant(data_list, dtype=dtypes.float64)
    indices = 3
    partitions = data_flow_ops.dynamic_partition(
        data, indices, num_partitions=4)
    partition_vals = self.evaluate(partitions)

self.assertEqual(4, len(partition_vals))
self.assertAllEqual(
    np.array([], dtype=np.float64).reshape(-1, 4), partition_vals[0])
self.assertAllEqual(
    np.array([], dtype=np.float64).reshape(-1, 4), partition_vals[1])
self.assertAllEqual(
    np.array([], dtype=np.float64).reshape(-1, 4), partition_vals[2])
self.assertAllEqual(
    np.array([10, 13, 12, 11], dtype=np.float64).reshape(-1, 4),
    partition_vals[3])
