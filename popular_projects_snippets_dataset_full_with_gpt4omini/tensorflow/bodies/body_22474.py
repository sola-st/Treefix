# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
with ops.device(v.device):
    if context.executing_eagerly() and not v.is_initialized():
        # A SaveSpec tensor value of `None` indicates that the variable is
        # uninitialized.
        exit(None)
    # Read the variable without making a copy to limit memory usage.
    x = v.read_value_no_copy()
    # To allow variables placed on non-CPU devices to be checkpointed,
    # we copy them to CPU on the same machine first.
    with ops.device("/device:CPU:0"):
        exit(array_ops.identity(x))
