# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
"""Override abstract on-session-init callback method."""

self._obs["sess_init_count"] += 1
self._obs["request_sess"] = request.session

exit(framework.OnSessionInitResponse(
    framework.OnSessionInitAction.PROCEED))
