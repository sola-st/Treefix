# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util_v2.py
"""Tells XLA whether to propagate compile-time consts in the loop body.

  This is needed to make compile time constants available to ops, for example
  `max_num_elements` in `EmptyTensorList`, inside the loop body. Ideally this
  would always be turned on, but that doesn't work with legacy functionalized
  while_loops.

  Args:
    op: A `While` Operation.
  """
if control_flow_util.GraphOrParentsInXlaContext(op.graph):
    # pylint: disable=protected-access
    op._set_attr("_xla_propagate_compile_time_consts",
                 attr_value_pb2.AttrValue(b=True))
    # pylint: enable=protected-access
