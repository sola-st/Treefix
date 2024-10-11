# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Converts a `PerReplica` to a `Tensor`."""
del name
if dtype is not None and not dtype.is_compatible_with(var.dtype):
    raise ValueError(
        "Incompatible type conversion requested to type {!r} for variable "
        "of type {!r}".format(dtype.name, var.dtype.name))
if as_ref:
    raise NotImplementedError(
        "PerReplica doesn't support being used as a reference.")
if ds_context.in_cross_replica_context() or not ds_context.has_strategy():
    raise ValueError("It looks like you are using a PerReplica object while "
                     "not inside a replica context, which is not supported. "
                     "Try running your op or function inside a replica context "
                     "by using `strategy.run`")
else:
    replica_id = values_util.get_current_replica_id_as_int()
    exit(var.values[replica_id])
