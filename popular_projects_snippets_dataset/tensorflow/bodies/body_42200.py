# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Blocks until all coordinated tasks are at the barrier.

    The barrier may fail if it times out or if one of the tasks is unhealthy.

    Args:
      barrier_id: Unique string identifying the barrier.
      timeout_in_ms: Duration before the barrier times out and fails.
    """
ensure_initialized()
pywrap_tfe.TFE_WaitAtBarrier(self._context_handle, barrier_id,
                             timeout_in_ms)
