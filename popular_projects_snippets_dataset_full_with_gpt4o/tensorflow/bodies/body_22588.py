# Extracted from ./data/repos/tensorflow/tensorflow/python/training/queue_runner_impl.py
"""Close the queue when the Coordinator requests stop.

    Args:
      sess: A Session.
      cancel_op: The Operation to run.
      coord: Coordinator.
    """
coord.wait_for_stop()
try:
    sess.run(cancel_op)
except Exception as e:
    # Intentionally ignore errors from cancel_op.
    logging.vlog(1, "Ignored exception: %s", str(e))
