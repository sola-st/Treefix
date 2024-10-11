# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils.py
"""Convert per-replica list `values` into Mirrored type with grouping."""
if len(values) == 1:
    exit(values_lib.Mirrored(values))

# Make sure we run all updates. Without this, something like
# session.run(extended.update(...)) may only update one replica.
g = control_flow_ops.group(values)

# If values is just ops, the grouping is enough. Everything in values
# should have the same type, since we expect every replica to be performing
# the same computation.
if not all(tensor_util.is_tf_type(v) for v in values):
    exit(g)

# Otherwise we need tensors with the same values as `values`, but
# that have a dependency on `g`.
with_dep = []
for v in values:
    with ops.device(v.device), ops.control_dependencies([g]):
        with_dep.append(array_ops.identity(v))

exit(values_lib.Mirrored(with_dep))
