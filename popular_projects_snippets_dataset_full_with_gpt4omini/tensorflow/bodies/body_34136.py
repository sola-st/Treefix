# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_partition_op_test.py
rows = 100000
cols = 100
data_list = [None] * rows
for i in range(rows):
    data_list[i] = [i for _ in range(cols)]
num_partitions = 97
indices_list = [(i**2) % num_partitions for i in range(rows)]
parts = [[] for _ in range(num_partitions)]
for i in range(rows):
    parts[(i**2) % num_partitions].append(data_list[i])
with self.session():
    data = constant_op.constant(data_list, dtype=dtypes.float32)
    indices = constant_op.constant(indices_list, dtype=dtypes.int32)
    partitions = data_flow_ops.dynamic_partition(
        data, indices, num_partitions=num_partitions)
    partition_vals = self.evaluate(partitions)

self.assertEqual(num_partitions, len(partition_vals))
for i in range(num_partitions):
    # reshape because of empty parts
    parts_np = np.array(parts[i], dtype=np.float64).reshape(-1, cols)
    self.assertAllEqual(parts_np, partition_vals[i])
