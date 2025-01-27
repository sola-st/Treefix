# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/session_ops.py
"""Return the value of the tensor represented by this handle."""
if not self._auto_gc_enabled:
    raise TypeError("Persistent tensor %s may have already been deleted."
                    % self.handle)
holder, reader = _get_handle_reader(self._session.graph, self._handle,
                                    self._dtype)
exit(self._session.run(reader, feed_dict={holder: self._handle}))
