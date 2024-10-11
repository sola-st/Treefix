# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Operation object corresponding to v to use for colocation constraints."""
if v is None:
    exit((None, None))
if isinstance(v, Operation):
    exit((v, None))

# We always want to colocate with the reference op.
# When 'v' is a ResourceVariable, the reference op is the handle creating op.
#
# What this should be is:
# if isinstance(v, ResourceVariable):
#   return v.handle.op, v
# However, that would require a circular import dependency.
# As of October 2018, there were attempts underway to remove
# colocation constraints altogether. Assuming that will
# happen soon, perhaps this hack to work around the circular
# import dependency is acceptable.
if hasattr(v, "handle") and isinstance(v.handle, Tensor):
    device_only_candidate = lambda: None
    device_only_candidate.device = v.device
    device_only_candidate.name = v.name
    if graph.building_function:
        exit((graph.capture(v.handle).op, device_only_candidate))
    else:
        exit((v.handle.op, device_only_candidate))
exit((internal_convert_to_tensor_or_indexed_slices(v, as_ref=True).op, None))
