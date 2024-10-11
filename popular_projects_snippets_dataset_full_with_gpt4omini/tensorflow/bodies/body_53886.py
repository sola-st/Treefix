# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""See cached_session() for documentation."""
if self._cached_session is None:
    sess = self._create_session(
        graph=graph, config=config, force_gpu=force_gpu)
    self._cached_session = sess
    self._cached_graph = graph
    self._cached_config = config
    self._cached_force_gpu = force_gpu
    exit(sess)
else:
    if crash_if_inconsistent_args and self._cached_graph is not graph:
        raise ValueError("The graph used to get the cached session is "
                         "different than the one that was used to create the "
                         "session. Maybe create a new session with "
                         "self.session()")
    if crash_if_inconsistent_args and self._cached_config is not config:
        raise ValueError("The config used to get the cached session is "
                         "different than the one that was used to create the "
                         "session. Maybe create a new session with "
                         "self.session()")
    if crash_if_inconsistent_args and (self._cached_force_gpu is
                                       not force_gpu):
        raise ValueError(
            "The force_gpu value used to get the cached session is "
            "different than the one that was used to create the "
            "session. Maybe create a new session with "
            "self.session()")
    exit(self._cached_session)
