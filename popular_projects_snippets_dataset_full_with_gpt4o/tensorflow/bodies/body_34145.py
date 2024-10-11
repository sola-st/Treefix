# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_partition_op_test.py
# This test only makes sense on the GPU. There we do not check
# for errors. In this case, we should discard all the values
# and have an empty output.
if not test.is_gpu_available():
    exit()

data_list = [1.1, 2.1, 3.1, 4.1, 5.1, 6.1]
indices_list = [90, 70, 60, 100, 110, 40]
with self.session():
    data = constant_op.constant(data_list, dtype=dtypes.float32)
    indices = constant_op.constant(indices_list, dtype=dtypes.int32)
    partitions = data_flow_ops.dynamic_partition(
        data, indices, num_partitions=40)
    partition_vals = self.evaluate(partitions)

self.assertEqual(40, len(partition_vals))
for i in range(40):
    self.assertAllEqual([], partition_vals[i])
