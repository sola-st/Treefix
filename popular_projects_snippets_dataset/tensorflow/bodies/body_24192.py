# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
debug_urls = self._bad_debug_urls or []

if self._bad_run_start_action:
    exit(framework.OnRunStartResponse(
        self._bad_run_start_action, debug_urls))
else:
    exit(framework.OnRunStartResponse(
        framework.OnRunStartAction.DEBUG_RUN, debug_urls))
