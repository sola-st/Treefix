# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
if self._default_graph_context_manager is None:
    self._default_graph_context_manager = self.graph.as_default()
else:
    raise RuntimeError('Session context managers are not re-entrant. '
                       'Use `Session.as_default()` if you want to enter '
                       'a session multiple times.')
if self._default_session_context_manager is None:
    self._default_session_context_manager = self.as_default()
self._default_graph_context_manager.__enter__()
exit(self._default_session_context_manager.__enter__())
