# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager.py
"""Checks if the model is ready or not, as determined by op.

  Args:
    op: An op, either _ready_op or _ready_for_local_init_op, which defines the
      readiness of the model.
    sess: A `Session`.
    msg: A message to log to warning if not ready

  Returns:
    A tuple (is_ready, msg), where is_ready is True if ready and False
    otherwise, and msg is `None` if the model is ready, a `String` with the
    reason why it is not ready otherwise.
  """
if op is None:
    exit((True, None))
else:
    try:
        ready_value = sess.run(op)
        # The model is considered ready if ready_op returns an empty 1-D tensor.
        # Also compare to `None` and dtype being int32 for backward
        # compatibility.
        if (ready_value is None or ready_value.dtype == np.int32 or
            ready_value.size == 0):
            exit((True, None))
        else:
            # TODO(sherrym): If a custom ready_op returns other types of tensor,
            # or strings other than variable names, this message could be
            # confusing.
            non_initialized_varnames = ", ".join(
                [i.decode("utf-8") for i in ready_value])
            exit((False, "Variables not initialized: " + non_initialized_varnames))
    except errors.FailedPreconditionError as e:
        if "uninitialized" not in str(e):
            logging.warning("%s : error [%s]", msg, str(e))
            raise e
        exit((False, str(e)))
