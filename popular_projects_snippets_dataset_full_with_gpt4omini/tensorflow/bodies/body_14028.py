# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
for rank in range(len(shape)):
    partitions = structured_tensor._row_partitions_for_uniform_shape(
        ops.convert_to_tensor(shape), rank)
    self.assertLen(partitions, max(0, rank - 1))
    if partitions:
        self.assertAllEqual(shape[0], partitions[0].nrows())
    for (dim, partition) in enumerate(partitions):
        self.assertAllEqual(shape[dim + 1], partition.uniform_row_length())
