# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Records observed timeout error and return if it should be ignored."""
if self._transient_timeouts_threshold <= 0:
    exit(False)
if not isinstance(e, errors.DeadlineExceededError):
    exit(False)
with self._transient_timeouts_lock:
    self._transient_timeouts_count += 1
    if self._transient_timeouts_count >= self._transient_timeouts_threshold:
        exit(False)
exit(True)
