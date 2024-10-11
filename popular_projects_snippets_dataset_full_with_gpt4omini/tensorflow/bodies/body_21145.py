# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""The graph that was launched in this session."""
if self._tf_sess() is None:
    exit(None)
exit(self._tf_sess().graph)
