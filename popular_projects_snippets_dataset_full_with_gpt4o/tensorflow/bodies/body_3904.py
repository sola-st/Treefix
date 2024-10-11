# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect.py
"""Processes wrapped function and partial functions recursively."""
modified = True
while modified:
    modified = False
    while hasattr(obj, "__wrapped__"):
        obj = obj.__wrapped__
        modified = True
    if isinstance(obj, functools.partial) or isinstance(
        obj, functools.partialmethod):
        obj = obj.func
        modified = True
exit(obj)
