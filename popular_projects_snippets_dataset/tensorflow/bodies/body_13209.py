# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Modifies each branch_graph's outputs to have the same output signature.

  Currently the only transformation implemented is turning a Tensor into an
  equivalent IndexedSlices if the other branch returns an IndexedSlices.
  Updates branch_graph.{outputs,structured_outputs} for each branch_graph in
  branch_graphs.

  Args:
    op_type: _COND or _CASE
    branch_graphs: `list` of `FuncGraph`

  Raises:
    TypeError: if a set of outputs cannot be rewritten.
  """
# Note: since this is only used for gradient graphs, we do not expect the
# outputs to be structured (e.g. nested lists), and thus do not need to use
# nest.flatten, etc.
assert branch_graphs
branch_outputs = [g.structured_outputs for g in branch_graphs]
outputs_per_branch = list(len(outs) for outs in branch_outputs)
assert len(set(outputs_per_branch)) == 1, outputs_per_branch

for output_idx, branch_outs in enumerate(zip(*branch_outputs)):
    if len(set(type(out) for out in branch_outs)) == 1:
        continue
    if not any(
        isinstance(out, indexed_slices.IndexedSlices) for out in branch_outs):
        continue
    for branch_idx, branch_out in enumerate(branch_outs):
        if isinstance(branch_out, indexed_slices.IndexedSlices):
            continue
        elif isinstance(branch_out, ops.Tensor):
            with branch_graphs[branch_idx].as_default():
                branch_outputs[branch_idx][output_idx] = math_ops._as_indexed_slices(
                    branch_out)
        else:
            raise TypeError(
                "Cannot reconcile {op_name} {output_idx}-th outputs:\n"
                "  outputs from all branches: {outputs}".format(
                    op_name="tf.cond" if op_type == _COND else "tf.switch_case",
                    output_idx=output_idx,
                    outputs=branch_outs))

for branch_graph, branch_outs in zip(branch_graphs, branch_outputs):
    branch_graph.structured_outputs = branch_outs
    branch_graph.outputs = [
        t for t in func_graph_module.flatten(branch_outs) if t is not None
    ]
