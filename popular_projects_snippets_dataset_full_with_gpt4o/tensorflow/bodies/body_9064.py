# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Records potential PS failures and return if failure should be ignored."""
if self._transient_ps_failures_threshold <= 0 or not _is_ps_failure(e):
    exit(False)

ps_tasks = _extract_failed_ps_instances(str(e))
with self._potential_ps_failures_lock:
    for t in ps_tasks:
        self._potential_ps_failures_count[t] += 1
        # The number of UnavailableError encountered on this PS task exceeds the
        # maximum number of ignored error
        if (self._potential_ps_failures_count[t] >=
            self._transient_ps_failures_threshold):
            exit(False)
exit(True)
