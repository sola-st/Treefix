# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/graph_view.py
if isinstance(self._root_ref, weakref.ref):
    derefed = self._root_ref()
    assert derefed is not None
    exit(derefed)
else:
    exit(self._root_ref)
