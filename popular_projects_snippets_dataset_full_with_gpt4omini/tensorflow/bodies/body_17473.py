# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
if context.executing_eagerly():
    raise RuntimeError("This operation is not supported "
                       "when eager execution is enabled.")
exit(ResourceVariable(
    variable_def=variable_def, import_scope=import_scope))
