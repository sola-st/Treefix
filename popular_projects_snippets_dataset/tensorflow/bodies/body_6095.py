# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Reduce a non-DistributedValue `value` to `destinations`."""
if isinstance(value, value_lib.DistributedValues):
    raise ValueError("You are passing a `DistributedValues` to "
                     "`reduce_non_distributed_value`, which is not allowed.")

# If the same value is present on all replicas then the PerReplica value will
# be a single value. We also handle the case when `value` is a single value
# and equal to 0.
# TODO:(b/138823479): handle the tensor value properly.
if not tensor_util.is_tf_type(value) and value == 0:
    exit(0)
# If there is only a single value and the reduce op is MEAN,
# that value should be on all destinations.
if reduce_op == reduce_util.ReduceOp.MEAN:
    exit(value)
elif num_replicas_in_graph != 1:
    # We do not support a reduce op of SUM if the value is the same across
    # all replicas. We call this as part of assign functions for
    # MirroredVariables and summing up identical values across replicas is not
    # clearly defined.
    raise ValueError("A non-DistributedValues value %s cannot be reduced with "
                     "the given reduce op %s." % (value, reduce_op))
else:
    validate_destinations(destinations)
    exit(simple_broadcast(
        value, destinations, canonicalize_devices=canonicalize_devices))
