# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Verify that a branch's tensor is not accessed in another branch fn."""
# Note: It is technically not possible for lower-branch_index branches to
# capture tensors from higher-branch_index branches, because of the order of
# branch graph construction, but we check all for completeness and to
# guard against potential future changes.
other_branch_graphs = {g: i for i, g in enumerate(branch_graphs)}
for i, branch_graph in enumerate(branch_graphs):
    for t in branch_graph.external_captures:
        if not isinstance(t, ops.EagerTensor) and t.graph in other_branch_graphs:
            branch_names = ["true_fn", "false_fn"] if op_type == _COND else [
                "branch {}".format(bi) for bi in range(len(branch_graphs))]
            raise ValueError(
                "Tensor {tname} in {b0name} is accessed from {b1name}.".format(
                    tname=t.name,
                    b0name=branch_names[other_branch_graphs[t.graph]],
                    b1name=branch_names[i]))
