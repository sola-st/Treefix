# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if var.aggregation == variables_lib.VariableAggregation.NONE:
    exit(update_fn(var._get_on_device_or_primary(), value, **kwargs))  # pylint: disable=protected-access
exit(_on_write_update_replica(var, update_fn, value, **kwargs))
