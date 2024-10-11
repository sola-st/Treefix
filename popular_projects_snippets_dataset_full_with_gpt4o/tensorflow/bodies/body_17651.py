# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/session_ops.py
"""Force the deletion of this persistent tensor."""
if not self._auto_gc_enabled:
    raise TypeError("Persistent tensor %s may have already been deleted."
                    % self.handle)
self._auto_gc_enabled = False
holder, deleter = _get_handle_deleter(self._session.graph, 0, self._handle)
self._session.run(deleter, feed_dict={holder: self.handle})
