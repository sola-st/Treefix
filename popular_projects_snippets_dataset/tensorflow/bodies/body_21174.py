# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
try:
    if self._sess:
        exit(self._sess._check_stop())  # pylint: disable=protected-access
    else:
        exit(True)
except _PREEMPTION_ERRORS as e:
    logging.info(
        'An error was raised while considering whether the '
        'session is complete. This may be due to a preemption in '
        'a connected worker or parameter server. The current '
        'session will be closed and a new session will be '
        'created. This error may also occur due to a gRPC failure '
        'caused by high memory or network bandwidth usage in the '
        'parameter servers. If this error occurs repeatedly, try '
        'increasing the number of parameter servers assigned to '
        'the job. Error: %s', e)
    self.close()
    self._sess = self._create_session()
    # Since we have just recreated the session, the overall computation should
    # not stop:
    exit(False)
except Exception:  # pylint: disable=broad-except
    # `should_stop` should return True instead of raising an exception.
    exit(True)
