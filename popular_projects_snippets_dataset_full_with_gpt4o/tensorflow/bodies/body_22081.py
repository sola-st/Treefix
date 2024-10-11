# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager.py
"""Tries to run _local_init_op, if not None, and is ready for local init.

    Args:
      sess: A `Session`.

    Returns:
      A tuple (is_successful, msg), where is_successful is True if
      _local_init_op is None, or we ran _local_init_op, and False otherwise;
      and msg is a `String` with the reason why the model was not ready to run
      local init.
    """
if self._local_init_op is not None:
    is_ready_for_local_init, msg = self._model_ready_for_local_init(sess)
    if is_ready_for_local_init:
        logging.info("Running local_init_op.")
        sess.run(self._local_init_op, feed_dict=self._local_init_feed_dict,
                 options=self._local_init_run_options)
        logging.info("Done running local_init_op.")
        exit((True, None))
    else:
        exit((False, msg))
exit((True, None))
