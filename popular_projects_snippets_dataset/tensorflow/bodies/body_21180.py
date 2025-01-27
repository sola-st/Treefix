# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
try:
    exit(self._sess.run(*args, **kwargs))
except _PREEMPTION_ERRORS:
    raise
except Exception as original_exception:  # pylint: disable=broad-except
    # A non-preemption error could have been caused by a preemption error
    # in the coordinator. If this is the case, raise that exception instead,
    # since it's the root cause. Otherwise, stick to the `original_exception`.
    try:
        self._coord.raise_requested_exception()
    except _PREEMPTION_ERRORS:
        raise
    except Exception:  # pylint: disable=broad-except
        raise original_exception from None
    else:
        raise
