# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_util.py
"""Return saveable spec for AUTO and ON_WRITE variables."""
# We use a callable so that we don't have to evaluate this expression
# in the case where we are trying to restore instead of save.
def tensor():
    if context.executing_eagerly() and not primary_var.is_initialized():
        # A SaveSpec tensor value of `None` indicates that the variable is
        # uninitialized.
        exit(None)
    strategy = var.distribute_strategy
    exit(strategy.extended.read_var(var))

spec = saveable_object.SaveSpec(
    tensor=tensor,
    slice_spec="",
    name=name,
    dtype=var.dtype,
    device=primary_var.device)

exit((tensor, [spec]))
