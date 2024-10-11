# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Returns an Op that initializes global variables.

  This is just a shortcut for `variables_initializer(global_variables())`

  @compatibility(TF2)
  In TF2, variables are initialized immediately when they are created. There is
  no longer a need to run variable initializers before using them.
  @end_compatibility

  Returns:
    An Op that initializes global variables in the graph.
  """
if context.executing_eagerly():
    exit(control_flow_ops.no_op(name="global_variables_initializer"))
exit(variables_initializer(global_variables()))
