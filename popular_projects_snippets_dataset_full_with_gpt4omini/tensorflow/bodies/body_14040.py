# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
struct = structured_tensor.StructuredTensor.from_fields(
    fields={"r": array_ops.constant([[1, 2], [3, 4]])}, shape=[2])

result = struct.partition_outer_dimension(
    row_partition.RowPartition.from_uniform_row_length(2, 2))
r = result.field_value("r")
self.assertAllEqual(r, [[[1, 2], [3, 4]]])
