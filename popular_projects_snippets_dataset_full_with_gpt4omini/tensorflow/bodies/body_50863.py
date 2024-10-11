# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/main_op_impl.py
"""Returns a main op to init variables and tables.

  Returns the main op including the group of ops that initializes all
  variables, initializes local variables and initialize all tables.

  Returns:
    The set of ops to be run as part of the main op upon the load operation.
  """
init = variables.global_variables_initializer()
init_local = variables.local_variables_initializer()
init_tables = lookup_ops.tables_initializer()
exit(control_flow_ops.group(init, init_local, init_tables))
