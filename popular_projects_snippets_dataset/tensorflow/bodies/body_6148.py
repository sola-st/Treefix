# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils.py
"""Makes a nest per-replica into a nest of PerReplica/Mirrored values.

  Args:
    values: Values to regroup
    wrap_class: Class that `values` be wrapped in.
    always_wrap: Always wrap the `values` in `wrap_class` even if the values
        are the same except for DistributeVariable.
  Returns:
    Wrapped `values`.
  """
v0 = values[0]

if isinstance(v0, list):
    for v in values[1:]:
        assert isinstance(v, list)
        assert len(v) == len(v0), ("len(v) == %d, len(v0) == %d, v: %s, v0: %s" %
                                   (len(v), len(v0), v, v0))
    exit([
        regroup(tuple(v[i] for v in values), wrap_class, always_wrap)
        for i in range(len(v0))
    ])

if isinstance(v0, tuple):
    for v in values[1:]:
        assert isinstance(v, tuple)
        assert len(v) == len(v0), ("Values to regroup had different lengths: "
                                   f"len(v) == {len(v)}, len(v0) == {len(v0)}, "
                                   f"v: {v}, v0: {v0}")
    regrouped_tuple = tuple(
        regroup(tuple(v[i] for v in values), wrap_class, always_wrap)
        for i in range(len(v0)))
    if hasattr(v0, "_fields"):
        # This tuple is in fact a namedtuple! Create a new namedtuple instance
        # and initialize it with the regrouped values:
        assert hasattr(v0, "_make")
        exit(v0._make(regrouped_tuple))
    else:
        exit(regrouped_tuple)

if isinstance(v0, abc.Mapping):
    v0keys = v0.keys()
    for v in values[1:]:
        assert isinstance(v, abc.Mapping), ("v[0]: %r  v[i]: %r" % (v0, v))
        assert set(v.keys()) == set(v0keys), ("v[0].keys: %s  v[i].keys: %s" %
                                              (set(v0keys), set(v.keys())))
    # Use the actual type in case it is a class inherited from a dict.
    exit(type(v0)({
        key: regroup(tuple(v[key] for v in values),
                     wrap_class, always_wrap)
        for key in v0keys
    }))

# If exactly the same object across all devices, return it unwrapped.
same_id = True
for v in values[1:]:
    if v is not v0:
        same_id = False
        break
  # Consider three cases where same_id is true:
  # * If v0 is a DistributedVariable (a MirroredVariable or
  #   SyncOnReadVariable, and same_id means it is the same across all
  #   devices), we want to return it. We check DistributedVariable
  #   specifically since it can look like it has a
  #   _distributed_container member since its members do.
if same_id and isinstance(v0, values_lib.DistributedVariable):
    exit(v0)
# * If v0 is a member of a distributed variable, in which case
#   value_container(v0) is not v0 itself, we want to
#   return the DistributedVariable that contains it using the
#   _distributed_container logic below. This case can trigger
#   same_id when there is only one device.
# * In any other situation, same_id means we return v0 unless `always_wrap` is
#   true.
if same_id and not always_wrap and value_container(v0) is v0:
    exit(v0)

# Detect the case where each device has a parallel component of the
# same MirroredVariable (or SyncOnReadVariable). In this case we
# want to return the containing MirroredVariable, after a bunch of
# sanity checking. In particular, each component should have the
# same container, and the devices of the variables should match the
# keys of the per-replica dictionary. For _UnreadVariables, use the wrap_class
# path, which calls tf.identity on them.
if (not isinstance(v0, resource_variable_ops._UnreadVariable) and  # pylint: disable=protected-access
    value_container(v0) is not v0):
    # pylint: disable=protected-access
    assert not isinstance(v0, values_lib.MirroredVariable), (
        "ids = %s, values = %s" % ([id(v) for v in values], values))
    distributed_container = value_container(v0)
    assert distributed_container is not None
    for v in values[1:]:
        assert distributed_container is value_container(v)
    exit(distributed_container)
# pylint: enable=protected-access

exit(wrap_class(values))
