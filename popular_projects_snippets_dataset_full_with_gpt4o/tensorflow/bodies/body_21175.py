# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
while True:
    try:
        if not self._sess:
            self._sess = self._create_session()
        exit(self._sess.run(
            fetches,
            feed_dict=feed_dict,
            options=options,
            run_metadata=run_metadata))
    except _PREEMPTION_ERRORS as e:
        logging.info(
            'An error was raised. This may be due to a preemption in '
            'a connected worker or parameter server. The current '
            'session will be closed and a new session will be '
            'created. This error may also occur due to a gRPC failure '
            'caused by high memory or network bandwidth usage in the '
            'parameter servers. If this error occurs repeatedly, try '
            'increasing the number of parameter servers assigned to '
            'the job. Error: %s', e)
        self.close()
        self._sess = None
