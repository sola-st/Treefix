# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
"""Override abstract on-run-start callback method."""

self._obs["on_run_start_count"] += 1
self._obs["run_fetches"] = request.fetches
self._obs["run_feed_dict"] = request.feed_dict

exit(framework.OnRunStartResponse(
    framework.OnRunStartAction.DEBUG_RUN,
    ["file://" + self._dump_root]))
