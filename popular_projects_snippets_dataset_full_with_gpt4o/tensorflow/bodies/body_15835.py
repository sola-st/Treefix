# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
if context.executing_eagerly():
    exit()
shape_a = DynamicRaggedShape.from_lengths(
    lengths_a, num_row_partitions=num_row_partitions_a)
result = shape_a._alt_inner_shape(new_inner_rank)
result_static = tensor_util.constant_value_as_shape(result)
self.assertEqual(inner_shape, result_static.as_list())
