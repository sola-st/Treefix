# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
if self._sess:
    try:
        self._sess.close()
    except _PREEMPTION_ERRORS as e:
        logging.error(
            'An error occurred when attempting to close the '
            'session. This may be due to a preemption in a '
            'connected worker or parameter server. Error: %s', e)
    finally:
        self._sess = None
