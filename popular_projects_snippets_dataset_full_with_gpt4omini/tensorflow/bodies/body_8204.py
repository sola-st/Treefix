# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
self.termination_watcher_fn = termination_watcher_fn
default_exit_fn = lambda: sys.exit(0)
self.exit_fn = exit_fn or default_exit_fn
self.grace_period = grace_period or 0
self.save_fn = save_fn
