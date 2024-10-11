# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
while True:
    try:
        exit(self._sess_creator.create_session())
    except _PREEMPTION_ERRORS as e:
        logging.info(
            'An error was raised while a session was being created. '
            'This may be due to a preemption of a connected worker '
            'or parameter server. A new session will be created. '
            'This error may also occur due to a gRPC failure caused '
            'by high memory or network bandwidth usage in the '
            'parameter servers. If this error occurs repeatedly, try '
            'increasing the number of parameter servers assigned to '
            'the job. Error: %s', e)
