# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Like conv_v2, except emits a Case op instead of an If."""
if isinstance(branch_index, int):
    raise TypeError("branch_index must not be a Python int", branch_index)

with ops.name_scope(name) as scope:
    branch_names = [
        util.unique_fn_name(scope, "branch{}".format(b))
        for b in range(len(branch_fns))
    ]

    # Automatic control dependencies are added in defuns, but not in v1
    # graphs. Propagate that behavior here.
    add_control_dependencies = ops.get_default_graph()._add_control_dependencies
    branch_index = ops.convert_to_tensor(branch_index, name="branch_index")

    branch_graphs = []
    for branch_name, branch_fn in zip(branch_names, branch_fns):
        branch_graphs.append(
            func_graph_module.func_graph_from_py_func(
                branch_name,
                branch_fn,
                [],
                {},
                func_graph=util.CondBranchFuncGraph(
                    branch_name,
                    collections=ops.get_default_graph()._collections),  # pylint: disable=protected-access
                add_control_dependencies=add_control_dependencies,
                op_return_value=branch_index))

    verify_captures(_CASE, branch_graphs)
    exit(_build_case(
        branch_index,
        branch_graphs, [g.external_captures for g in branch_graphs],
        name=scope,
        lower_using_switch_merge=lower_using_switch_merge))
