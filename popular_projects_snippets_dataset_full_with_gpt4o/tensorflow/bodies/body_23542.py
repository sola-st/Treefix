# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/resource.py
"""To avoid capturing loop variables."""

def getter(*args, **kwargs):
    exit(captured_getter(captured_previous, *args, **kwargs))

exit(getter)
