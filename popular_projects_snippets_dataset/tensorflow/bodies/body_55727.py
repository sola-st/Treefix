# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/graph_building_test.py
with func_graph.FuncGraph("resource").as_default():
    handle = resource_variable_ops.var_handle_op(
        dtype=dtypes.int32, shape=[])
    resource_variable_ops.assign_variable_op(
        handle, constant_op.constant(1, dtype=dtypes.int32))
    for _ in range(num_ops):
        gen_resource_variable_ops.read_variable_op(handle, dtype=dtypes.int32)
