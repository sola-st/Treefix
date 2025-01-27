# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Merge the inner shape of a DynamicRaggedShape."""
prefix = inner_shape[:outer_axis]
suffix = inner_shape[inner_axis + 1:]

internal = inner_shape[outer_axis:inner_axis + 1]
internal_value = [_reduce_prod_patch(internal)]
new_internal = array_ops.concat([prefix, internal_value, suffix], axis=0)
prefix_static = static_inner_shape[:outer_axis]
suffix_static = static_inner_shape[inner_axis + 1:]
internal_static = static_inner_shape[outer_axis:inner_axis + 1]
internal_value_static = tensor_shape.TensorShape(
    [internal_static.num_elements()])
new_internal_static = prefix_static + internal_value_static + suffix_static

exit((new_internal, new_internal_static))
