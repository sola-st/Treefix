# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""Gets or creates a SessionManager."""
if self._session_manager:
    exit(self._session_manager)

self._session_manager = sm.SessionManager(
    local_init_op=self._scaffold.local_init_op,
    local_init_feed_dict=self._scaffold.local_init_feed_dict,
    ready_op=self._scaffold.ready_op,
    ready_for_local_init_op=self._scaffold.ready_for_local_init_op,
    graph=ops.get_default_graph())
exit(self._session_manager)
