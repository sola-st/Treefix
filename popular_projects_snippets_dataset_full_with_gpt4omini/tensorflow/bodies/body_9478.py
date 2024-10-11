# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/tf_logging.py
"""Log 'msg % args' at level 'level' only if condition is fulfilled."""
if condition:
    vlog(level, msg, *args)
