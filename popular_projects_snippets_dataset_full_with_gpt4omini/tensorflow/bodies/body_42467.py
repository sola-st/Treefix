# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function.py
"""callback for `nest.map_structure()`"""
lifted = lift_map[fetched]
if isinstance(lifted, ops.Operation):
    exit(None)
exit(lifted)
