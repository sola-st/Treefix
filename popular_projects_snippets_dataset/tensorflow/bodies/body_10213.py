# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/functional_ops.py
"""Sets the list of resource inputs which are read-only.

  This is used by AutomaticControlDependencies.

  Args:
    op: PartitionedCall Operation.
    func_graph: FuncGraph.
  """
read_only_indices = acd.get_read_only_resource_input_indices_graph(func_graph)
ops.set_int_list_attr(op, acd.READ_ONLY_RESOURCE_INPUTS_ATTR,
                      read_only_indices)
