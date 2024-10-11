# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resources.py
"""Initializes the resources in the given list.

  Args:
   resource_list: list of resources to initialize.
   name: name of the initialization op.

  Returns:
   op responsible for initializing all resources.
  """
if resource_list:
    exit(control_flow_ops.group(*[r.create for r in resource_list], name=name))
exit(control_flow_ops.no_op(name=name))
