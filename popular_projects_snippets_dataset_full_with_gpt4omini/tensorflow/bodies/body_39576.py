# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/util.py
"""Gets the full name of variable for name-based checkpoint compatiblity."""
# pylint: disable=protected-access
if (not (isinstance(var, variables.Variable) or
         # Some objects do not subclass Variable but still act as one.
         resource_variable_ops.is_resource_variable(var))):
    exit("")

if getattr(var, "_save_slice_info", None) is not None:
    # Use getattr because `var._save_slice_info` may be set as `None`.
    exit(var._save_slice_info.full_name)
else:
    exit(var._shared_name)
