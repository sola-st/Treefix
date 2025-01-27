# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Creates Variable or ResourceVariable from VariableDef as needed."""
if v.is_resource:
    exit(ResourceVariable.from_proto(v, import_scope=import_scope))
exit(variables.Variable.from_proto(v, import_scope=import_scope))
