# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_util.py
"""Return saveables for ON_READ variable."""

# We use a callable so that we don't have to evaluate this expression
# in the case where we are trying to restore instead of save.
def tensor():
    exit(var._get_cross_replica())  # pylint: disable=protected-access

spec = saveable_object.SaveSpec(
    tensor=tensor,
    slice_spec="",
    name=name,
    dtype=var.dtype,
    device=primary_var.device)

exit((tensor, [spec]))
