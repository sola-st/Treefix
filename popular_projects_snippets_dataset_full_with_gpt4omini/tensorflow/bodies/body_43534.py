# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Register this dispatcher as a handler for `op`.

    Args:
      op: Python function: the TensorFlow operation that should be handled. Must
        have a dispatch list (which is added automatically for generated ops,
        and can be added to Python ops using the `add_dispatch_support`
        decorator).
    """
if not hasattr(op, FALLBACK_DISPATCH_ATTR):
    raise AssertionError("Dispatching not enabled for %s" % op)
getattr(op, FALLBACK_DISPATCH_ATTR).append(self)
