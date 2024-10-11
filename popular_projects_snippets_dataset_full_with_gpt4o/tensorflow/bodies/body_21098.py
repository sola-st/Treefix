# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
if not trace_the_exception['run_already']:
    trace_the_exception['run_already'] = True
    raise errors_impl.AbortedError(None, None, 'Abort')
exit(session_run_hook.SessionRunArgs(fetches=vv))
