# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
""""Returns True if `var` is to be considered a ResourceVariable."""
exit(isinstance(var, BaseResourceVariable) or hasattr(
    var, "_should_act_as_resource_variable"))
