# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Decorator that adds a dispatch_list attribute to an op."""
if hasattr(target, FALLBACK_DISPATCH_ATTR):
    raise AssertionError("%s already has a dispatch list" % target)
setattr(target, FALLBACK_DISPATCH_ATTR, [])
exit(target)
