# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
if context.executing_eagerly():
    exit()

shape_a0 = DynamicRaggedShape.from_lengths(
    lengths_a, num_row_partitions=num_row_partitions_a)
shape_b0 = DynamicRaggedShape.from_lengths(
    lengths_b, num_row_partitions=num_row_partitions_b)
rt_a = ragged_array_ops.ragged_reshape(
    _lowest_primes(_num_elements_of_lengths(lengths_a)), shape_a0)
rt_b = ragged_array_ops.ragged_reshape(
    _lowest_primes(_num_elements_of_lengths(lengths_b)), shape_b0)
g = rt_a.flat_values.graph if ragged_tensor.is_ragged(rt_a) else rt_a.graph

nodes_at_a = len(g.as_graph_def().node)
if new_impl:
    dynamic_ragged_shape.ragged_binary_elementwise_op_impl(
        gen_math_ops.add_v2,
        rt_a,
        rt_b)
    nodes_at_b = len(g.as_graph_def().node)
    num_nodes = nodes_at_b - nodes_at_a
    self.assertLessEqual(num_nodes, max_num_ops)
else:
    if isinstance(rt_a, RaggedTensor):
        rt_a = rt_a.with_row_splits_dtype(dtypes.int32)
    if isinstance(rt_b, RaggedTensor):
        rt_b = rt_b.with_row_splits_dtype(dtypes.int32)
    nodes_at_b = len(g.as_graph_def().node)
    rt_a + rt_b  # pylint: disable=pointless-statement
    nodes_at_d = len(g.as_graph_def().node)
    num_nodes = nodes_at_d - nodes_at_b
