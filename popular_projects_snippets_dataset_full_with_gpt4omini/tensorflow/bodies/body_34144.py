# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_partition_op_test.py
# This test only makes sense on the GPU. There we do not check
# for errors. In this case, we should discard all the values
# larger than num_partitions.
if not test.is_gpu_available():
    exit()

data_list = [1, 2, 3, 4, 5, 6]
indices_list = [10, 11, 2, 12, 0, 1000]
with self.session():
    data = constant_op.constant(data_list, dtype=dtypes.float32)
    indices = constant_op.constant(indices_list, dtype=dtypes.int32)
    partitions = data_flow_ops.dynamic_partition(
        data, indices, num_partitions=5)
    partition_vals = self.evaluate(partitions)

self.assertEqual(5, len(partition_vals))
self.assertAllEqual([5], partition_vals[0])
self.assertAllEqual([], partition_vals[1])
self.assertAllEqual([3], partition_vals[2])
self.assertAllEqual([], partition_vals[3])
self.assertAllEqual([], partition_vals[4])
