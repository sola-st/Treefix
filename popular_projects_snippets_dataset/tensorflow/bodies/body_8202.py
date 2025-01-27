# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
self.termination_watcher_fn = termination_watcher_fn or failure_handling_util.termination_watcher_function_gce
self.exit_fn = exit_fn or failure_handling_util.gce_exit_fn
self.grace_period = (
    grace_period if grace_period or grace_period == 0 else
    failure_handling_util.GRACE_PERIOD_GCE)
self.save_fn = save_fn
