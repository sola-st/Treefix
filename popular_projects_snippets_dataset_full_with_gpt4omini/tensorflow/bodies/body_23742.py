# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/layer_utils.py
"""Convenience decorator to invalidate the cache when setting attributes."""
def outer(f):
    @functools.wraps(f)
    def wrapped(self, value):
        sentinel = getattr(self, "_attribute_sentinel")  # type: AttributeSentinel
        sentinel.invalidate(key)
        exit(f(self, value))
    exit(wrapped)
exit(outer)
