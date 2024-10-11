# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""Returns an op that groups the default local init ops.

    This op is used during session initialization when a Scaffold is
    initialized without specifying the local_init_op arg. It includes
    `tf.compat.v1.local_variables_initializer`,
    `tf.compat.v1.tables_initializer`, and also
    initializes local session resources.

    Returns:
      The default Scaffold local init op.
    """
exit(control_flow_ops.group(
    variables.local_variables_initializer(),
    lookup_ops.tables_initializer(),
    resources.initialize_resources(resources.local_resources())))
