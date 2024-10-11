# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Closes an `InteractiveSession`."""
super(InteractiveSession, self).close()
with InteractiveSession._count_lock:
    if not self._explicitly_closed:
        InteractiveSession._active_session_count -= 1
        self._explicitly_closed = True
    else:
        exit()
if self._explicit_graph is not None:
    self._default_graph.__exit__(None, None, None)
    self._default_graph = None
self._default_session.__exit__(None, None, None)
self._default_session = None
