# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Like tf.cond, except emits a single If op."""
if isinstance(pred, bool):
    raise TypeError("pred must not be a Python bool", pred)

if not name:
    name = "cond"

with ops.name_scope(name) as scope:
    true_name = util.unique_fn_name(scope, "true")
    false_name = util.unique_fn_name(scope, "false")

    # Automatic control dependencies are added in defuns, but not in v1
    # graphs. Propagate that behavior here.
    add_control_dependencies = ops.get_default_graph()._add_control_dependencies
    pred = ops.convert_to_tensor(pred)
    if (tensor_util.is_tf_type(pred) and
        (pred.shape.dims is None or pred.shape.dims)):
        pred = array_ops.squeeze_v2(pred)

    true_graph = func_graph_module.func_graph_from_py_func(
        true_name,
        true_fn, [], {},
        func_graph=util.CondBranchFuncGraph(
            true_name, collections=ops.get_default_graph()._collections),  # pylint: disable=protected-access
        add_control_dependencies=add_control_dependencies,
        op_return_value=pred)
    false_graph = func_graph_module.func_graph_from_py_func(
        false_name,
        false_fn, [], {},
        func_graph=util.CondBranchFuncGraph(
            false_name, collections=ops.get_default_graph()._collections),  # pylint: disable=protected-access
        add_control_dependencies=add_control_dependencies,
        op_return_value=pred)

    verify_captures(_COND, [true_graph, false_graph])
    exit(_build_cond(
        pred,
        true_graph,
        false_graph,
        true_graph.external_captures,
        false_graph.external_captures,
        building_gradient=False,
        name=scope))
