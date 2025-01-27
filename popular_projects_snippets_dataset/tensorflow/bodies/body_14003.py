# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
"""Sets the list of resource inputs which are read-only.

  This is used by AutomaticControlDependencies.

  Args:
    op: While Operation.
    branch_graphs: List of branch FuncGraphs.
  """
read_only_indices = set(range(len(op.inputs)))
for branch_graph in branch_graphs:
    if not read_only_indices:
        break
    branch_read_only_indices = acd.get_read_only_resource_input_indices_graph(
        branch_graph)
    read_only_indices = read_only_indices.intersection(branch_read_only_indices)

ops.set_int_list_attr(op, acd.READ_ONLY_RESOURCE_INPUTS_ATTR,
                      sorted(read_only_indices))
