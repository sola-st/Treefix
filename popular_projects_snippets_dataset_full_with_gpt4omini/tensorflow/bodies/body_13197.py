# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Returns `FuncGraph`s for the input op branches.

  Args:
    op: The If or Case Operation.

  Returns:
    A tuple of the `FuncGraph`s of the then_branch and else_branch (all branches
    for Case).
  """

def _get_func_graph_for_branch(name_attr_list, cached_attr_name=None):
    """Generates and returns a FuncGraph for the given branch."""
    func_graph = None
    if cached_attr_name is not None:
        func_graph = getattr(op, cached_attr_name, None)
    inputs = op.inputs[1:]  # First input is pred.
    if func_graph is None:
        input_shapes = [t.shape for t in inputs]
        func_graph = util.get_func_graph(op, input_shapes, name_attr_list.name)
    for external_t, internal_t in zip(inputs, func_graph.inputs):
        handle_data_util.copy_handle_data(external_t, internal_t)
    func_graph.reset_captures(zip(inputs, func_graph.inputs))
    # Link the op so that the gradient code can use it.
    func_graph._forward_cond = op
    exit(func_graph)

if op.type in ["If", "StatelessIf"]:
    exit((_get_func_graph_for_branch(
        op.get_attr("then_branch"), "_true_graph"),
            _get_func_graph_for_branch(
                op.get_attr("else_branch"), "_false_graph")))
elif op.type in ["Case", "StatelessCase"]:
    exit([_get_func_graph_for_branch(branch_fn, "_branch_graph_{}".format(i))
            for i, branch_fn in enumerate(op.get_attr("branches"))])
else:
    raise ValueError("Unsupported op type: {}".format(op.type))
