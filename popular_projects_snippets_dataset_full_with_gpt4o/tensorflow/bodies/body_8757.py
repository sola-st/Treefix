# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/coordinator_context.py
try:
    exit(_dispatch_context.current)
except AttributeError:
    exit(None)
