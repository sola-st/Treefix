# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager.py
"""Creates a SessionManager.

    The `local_init_op` is an `Operation` that is run always after a new session
    was created. If `None`, this step is skipped.

    The `ready_op` is an `Operation` used to check if the model is ready.  The
    model is considered ready if that operation returns an empty 1D string
    tensor. If the operation returns a non empty 1D string tensor, the elements
    are concatenated and used to indicate to the user why the model is not
    ready.

    The `ready_for_local_init_op` is an `Operation` used to check if the model
    is ready to run local_init_op.  The model is considered ready if that
    operation returns an empty 1D string tensor. If the operation returns a non
    empty 1D string tensor, the elements are concatenated and used to indicate
    to the user why the model is not ready.

    If `ready_op` is `None`, the model is not checked for readiness.

    `recovery_wait_secs` is the number of seconds between checks that
    the model is ready.  It is used by processes to wait for a model to
    be initialized or restored.  Defaults to 30 seconds.

    Args:
      local_init_op: An `Operation` run immediately after session creation.
         Usually used to initialize tables and local variables.
      ready_op: An `Operation` to check if the model is initialized.
      ready_for_local_init_op: An `Operation` to check if the model is ready
         to run local_init_op.
      graph: The `Graph` that the model will use.
      recovery_wait_secs: Seconds between checks for the model to be ready.
      local_init_run_options: RunOptions to be passed to session.run when
        executing the local_init_op.
      local_init_feed_dict: Optional session feed dictionary to use when running
        the local_init_op.

    Raises:
      ValueError: If ready_for_local_init_op is not None but local_init_op is
        None
    """
# Sets default values of arguments.
if graph is None:
    graph = ops.get_default_graph()
self._local_init_op = local_init_op
self._ready_op = ready_op
self._ready_for_local_init_op = ready_for_local_init_op
self._graph = graph
self._recovery_wait_secs = recovery_wait_secs
self._target = None
self._local_init_run_options = local_init_run_options
self._local_init_feed_dict = local_init_feed_dict
if ready_for_local_init_op is not None and local_init_op is None:
    raise ValueError("If you pass a ready_for_local_init_op "
                     "you must also pass a local_init_op "
                     ", ready_for_local_init_op [%s]" %
                     ready_for_local_init_op)
