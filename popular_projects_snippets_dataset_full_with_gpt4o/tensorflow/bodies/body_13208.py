# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Creates zeros for None out grads if at least one branch has non-None grad.

  Args:
    forward_graphs: List of forward FuncGraphs.
    grad_graphs: List of grad FuncGraphs.
  """
assert len(forward_graphs) == len(grad_graphs)
branch_outputs = [g.structured_outputs for g in grad_graphs]
num_outputs_per_branch = [len(outs) for outs in branch_outputs]
assert len(set(num_outputs_per_branch)) == 1, num_outputs_per_branch
for output_idx, branch_outs in enumerate(zip(*branch_outputs)):
    if (any(t is None for t in branch_outs) and
        any(t is not None for t in branch_outs)):
        for branch_index, t in enumerate(branch_outs):
            if t is None:
                with grad_graphs[branch_index].as_default():
                    zeros = default_gradient.zeros_like(
                        forward_graphs[branch_index].inputs[output_idx])
                    grad_graphs[branch_index].structured_outputs[output_idx] = zeros

for grad_graph in grad_graphs:
    grad_graph.outputs = [
        t for t in func_graph_module.flatten(grad_graph.structured_outputs)
        if t is not None
    ]
