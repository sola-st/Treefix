# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Default variable creator."""
assert next_creator is None
initial_value = kwargs.get("initial_value", None)
trainable = kwargs.get("trainable", None)
validate_shape = kwargs.get("validate_shape", True)
caching_device = kwargs.get("caching_device", None)
name = kwargs.get("name", None)
variable_def = kwargs.get("variable_def", None)
dtype = kwargs.get("dtype", None)
import_scope = kwargs.get("import_scope", None)
constraint = kwargs.get("constraint", None)
distribute_strategy = kwargs.get("distribute_strategy", None)
synchronization = kwargs.get("synchronization", None)
aggregation = kwargs.get("aggregation", None)
shape = kwargs.get("shape", None)
experimental_enable_variable_lifting = kwargs.get(
    "experimental_enable_variable_lifting", None)

exit(resource_variable_ops.ResourceVariable(
    initial_value=initial_value,
    trainable=trainable,
    validate_shape=validate_shape,
    caching_device=caching_device,
    name=name,
    dtype=dtype,
    constraint=constraint,
    variable_def=variable_def,
    import_scope=import_scope,
    distribute_strategy=distribute_strategy,
    synchronization=synchronization,
    aggregation=aggregation,
    shape=shape,
    experimental_enable_variable_lifting=experimental_enable_variable_lifting,
    ))
