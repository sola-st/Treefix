# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/trace.py
if enabled:
    with Trace(trace_name, **trace_kwargs):
        exit(func(*args, **kwargs))
exit(func(*args, **kwargs))
