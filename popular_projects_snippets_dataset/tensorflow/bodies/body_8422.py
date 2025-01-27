# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
assert isinstance(var, tpu_values.TPUVariableMixin) or isinstance(
    var, resource_variable_ops.BaseResourceVariable)
exit(var.read_value())
