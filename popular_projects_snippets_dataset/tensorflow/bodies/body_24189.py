# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
"""Override abstract on-run-end callback method."""

self._obs["on_run_end_count"] += 1
self._obs["performed_action"] = request.performed_action
self._obs["tf_error"] = request.tf_error

exit(framework.OnRunEndResponse())
