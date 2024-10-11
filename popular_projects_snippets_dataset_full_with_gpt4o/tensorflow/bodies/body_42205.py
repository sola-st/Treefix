# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Check collective peer health.

    This probes each task to see if they're still alive. Note that restarted
    tasks are considered a different one, and they're considered not healthy.

    This should only be used in multi client multi worker training.

    Args:
      task: a task string, must be in the format of /job:xxx/replica:0/task:N.
      timeout_in_ms: an integer, the timeout. If zero, there's no timeout.

    Raises:
      tf.errors.UnavailableError: when a peer is down.
      tf.errors.FailedPreconditionError: when a peer is a different one from the
        one this task has talked to, e.g. the peer has restarted.
      tf.errors.InvalidArgumentError: when the task string is invalid.
    """
self.ensure_initialized()
pywrap_tfe.TFE_CollectiveOpsCheckPeerHealth(self._handle, task,
                                            timeout_in_ms)
