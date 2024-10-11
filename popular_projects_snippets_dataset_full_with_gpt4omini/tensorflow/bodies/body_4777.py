# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
if isinstance(var, ps_values.AggregatingVariable):
    var = var.get()
if not resource_variable_ops.is_resource_variable(var):
    raise ValueError(
        "You can not update `var` %r. It must be a Variable." % var)
with ops.colocate_with(var), distribute_lib.UpdateContext(var.device):
    result = fn(var, *self._select_single_value(args),
                **self._select_single_value(kwargs))
    if group:
        exit(result)
    else:
        exit(nest.map_structure(self._local_results, result))
