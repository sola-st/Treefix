# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Initializes local_init_op.

    Args:
      local_init_op: `Operation` run for every new supervisor instance. If set
        to USE_DEFAULT, use the first op from the GraphKeys.LOCAL_INIT_OP
        collection. If the collection is empty, create an op that initializes
        all local variables and all tables.
    """
if local_init_op is Supervisor.USE_DEFAULT:
    local_init_op = self._get_first_op_from_collection(
        ops.GraphKeys.LOCAL_INIT_OP)
    if local_init_op is None:
        op_list = [
            variables.local_variables_initializer(),
            lookup_ops.tables_initializer()
        ]
        if op_list:
            local_init_op = control_flow_ops.group(*op_list)
            ops.add_to_collection(ops.GraphKeys.LOCAL_INIT_OP, local_init_op)
self._local_init_op = local_init_op
