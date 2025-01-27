# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
if context.executing_eagerly():
    exit()
shape_a = DynamicRaggedShape.from_lengths(
    lengths_a, num_row_partitions=num_row_partitions_a)
shape_b = DynamicRaggedShape.from_lengths(
    lengths_b, num_row_partitions=num_row_partitions_b)

result = dynamic_ragged_shape.broadcast_dynamic_shape(shape_a, shape_b)
result_shape = result._to_tensor_shape()

tensor_shape_e = [None if isinstance(x, tuple) else x for x in shape_e]
self.assertEqual(shape_e, result.static_lengths())
self.assertEqual(tensor_shape_e, result_shape.as_list())
