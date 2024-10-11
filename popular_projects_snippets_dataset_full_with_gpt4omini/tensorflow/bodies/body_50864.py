# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/main_op_impl.py
"""Returns a main op to init variables, tables and restore the graph.

  Returns the main op including the group of ops that initializes all
  variables, initialize local variables, initialize all tables and the restore
  op name.

  Args:
    restore_op_name: Name of the op to use to restore the graph.

  Returns:
    The set of ops to be run as part of the main op upon the load operation.
  """
with ops.control_dependencies([main_op()]):
    main_op_with_restore = control_flow_ops.group(restore_op_name)
exit(main_op_with_restore)
