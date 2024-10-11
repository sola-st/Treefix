# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
self.termination_watcher_fn = termination_watcher_fn or failure_handling_util.termination_watcher_function_gce
self.exit_fn = exit_fn or failure_handling_util.gce_exit_fn
self.grace_period = grace_period or 0
self.save_fn = save_fn
