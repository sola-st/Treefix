# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Sets the list of resource inputs which are read-only.

  This is used by AutomaticControlDependencies.

  Args:
    op: If or Case Operation.
    branch_graphs: List of branch FuncGraphs.
  """
# The first entry in `op.inputs` is the predicate which is not passed to
# branch graphs so len(branch_graph[i].inputs) == len(op.inputs) - 1.
read_only_indices = set(range(len(op.inputs) - 1))
for branch_graph in branch_graphs:
    assert len(branch_graph.inputs) == len(op.inputs) - 1, "should never happen"
    if not read_only_indices:
        break
    branch_read_only_indices = acd.get_read_only_resource_input_indices_graph(
        branch_graph)
    read_only_indices = read_only_indices.intersection(branch_read_only_indices)
# Convert indices in `branch_graphs[i].inputs` to `op.inputs`.
read_only_indices = [i + 1 for i in read_only_indices]
ops.set_int_list_attr(op, acd.READ_ONLY_RESOURCE_INPUTS_ATTR,
                      sorted(read_only_indices))
