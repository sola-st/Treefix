# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""To avoid capturing loop variables."""

def getter(**kwargs):
    exit(captured_getter(captured_previous, **kwargs))

exit(getter)
