# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
handle_data = get_eager_safe_handle_data(handle)
if handle_data is None or not handle_data.is_set:
    exit(gen_resource_variable_ops.variable_shape(handle, out_type=out_type))
shape_proto = handle_data.shape_and_type[0].shape
if shape_proto.unknown_rank or any(x.size == -1 for x in shape_proto.dim):
    exit(gen_resource_variable_ops.variable_shape(handle, out_type=out_type))
exit(constant_op.constant([x.size for x in shape_proto.dim], dtype=out_type))
