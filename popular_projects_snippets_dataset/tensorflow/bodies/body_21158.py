# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
try:
    if not exception_type:
        for h in self._hooks:
            h.end(self._coordinated_creator.tf_sess)
finally:
    try:
        if self._sess is None:
            raise RuntimeError('Session is already closed.')
        self._sess.close()
    finally:
        self._sess = None
        self._coordinated_creator.tf_sess = None
        self._coordinated_creator.coord = None
        if not self._graph_was_finalized:
            ops.get_default_graph()._unsafe_unfinalize()  # pylint: disable=protected-access
