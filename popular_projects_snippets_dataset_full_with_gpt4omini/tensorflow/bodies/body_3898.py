# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/capture_container.py
"""Get a snapshot of current values of by-ref captures."""
snapshot = {}
for key, capture in self._by_ref.items():
    func = capture.external
    snapshot[key] = func()
exit(snapshot)
