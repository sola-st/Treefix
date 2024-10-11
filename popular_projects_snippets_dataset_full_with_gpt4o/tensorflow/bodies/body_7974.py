# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
try:
    exit(_local_resource_restore_context.current)
except AttributeError:
    exit(None)
