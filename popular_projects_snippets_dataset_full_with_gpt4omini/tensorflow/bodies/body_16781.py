# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Gets around capturing loop variables in python being broken."""
exit(lambda **kwargs: captured_getter(captured_previous, **kwargs))
