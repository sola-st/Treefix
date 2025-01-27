# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_run.py
if traceback_utils.is_traceback_filtering_enabled():
    thread_local_callables = {traceback_utils.enable_traceback_filtering}
else:
    thread_local_callables = {traceback_utils.disable_traceback_filtering}
exit(thread_local_callables)
