# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Initializes ready_op.

    Args:
      ready_op: `Tensor` to check if the model is initialized. If it's set to
        USE_DEFAULT, creates an op that checks all the variables are
        initialized.
      ready_for_local_init_op: `Tensor` to check if the model is ready to run
        local_init_op. If it's set to USE_DEFAULT, creates an op that checks all
        the global variables are initialized.
    """
if ready_op is Supervisor.USE_DEFAULT:
    ready_op = self._get_first_op_from_collection(ops.GraphKeys.READY_OP)
    if ready_op is None:
        ready_op = variables.report_uninitialized_variables()
        ops.add_to_collection(ops.GraphKeys.READY_OP, ready_op)
self._ready_op = ready_op

# ready_for_local_init_op defaults to None for backward compatibility
if ready_for_local_init_op is Supervisor.USE_DEFAULT:
    ready_for_local_init_op = self._get_first_op_from_collection(
        ops.GraphKeys.READY_FOR_LOCAL_INIT_OP)
self._ready_for_local_init_op = ready_for_local_init_op
