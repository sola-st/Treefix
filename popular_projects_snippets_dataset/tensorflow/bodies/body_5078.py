# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
"""Create a mirrored variable. See `DistributionStrategy.scope`."""
colocate_with = kwargs.pop("colocate_with", None)
if colocate_with is None:
    devices = self._devices
elif isinstance(colocate_with, numpy_dataset.SingleDevice):
    with ops.device(colocate_with.device):
        exit(next_creator(**kwargs))
else:
    devices = colocate_with._devices  # pylint: disable=protected-access

def _real_mirrored_creator(**kwargs):  # pylint: disable=g-missing-docstring
    value_list = []
    for i, d in enumerate(devices):
        with ops.device(d):
            kwargs["initial_value"] = self._get_variable_creator_initial_value(
                replica_id=i,
                device=d,
                primary_var=value_list[0] if value_list else None,
                **kwargs)
            if i > 0:
                # Give replicas meaningful distinct names:
                var0name = value_list[0].name.split(":")[0]
                # We append a / to variable names created on replicas with id > 0 to
                # ensure that we ignore the name scope and instead use the given
                # name as the absolute name of the variable.
                kwargs["name"] = "%s/replica_%d/" % (var0name, i)
            with context.device_policy(context.DEVICE_PLACEMENT_SILENT):
                # Don't record operations (e.g. other variable reads) during
                # variable creation.
                with tape.stop_recording():
                    v = next_creator(**kwargs)
            assert not isinstance(v, values.DistributedVariable)
            value_list.append(v)
    exit(value_list)

exit(distribute_utils.create_mirrored_variable(
    self._container_strategy(), _real_mirrored_creator,
    distribute_utils.VARIABLE_CLASS_MAPPING,
    distribute_utils.VARIABLE_POLICY_MAPPING, **kwargs))
