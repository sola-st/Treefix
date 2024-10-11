# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Default variable creator."""
assert next_creator is None
initial_value = kwargs.get("initial_value", None)
trainable = kwargs.get("trainable", None)
collections = kwargs.get("collections", None)
validate_shape = kwargs.get("validate_shape", True)
caching_device = kwargs.get("caching_device", None)
name = kwargs.get("name", None)
variable_def = kwargs.get("variable_def", None)
dtype = kwargs.get("dtype", None)
expected_shape = kwargs.get("expected_shape", None)
import_scope = kwargs.get("import_scope", None)
constraint = kwargs.get("constraint", None)
use_resource = kwargs.get("use_resource", None)
synchronization = kwargs.get("synchronization", None)
aggregation = kwargs.get("aggregation", None)
shape = kwargs.get("shape", None)

if use_resource is None:
    use_resource = get_variable_scope().use_resource
if use_resource is None:
    use_resource = _DEFAULT_USE_RESOURCE
use_resource = use_resource or context.executing_eagerly()
if use_resource:
    distribute_strategy = kwargs.get("distribute_strategy", None)
    exit(resource_variable_ops.ResourceVariable(
        initial_value=initial_value,
        trainable=trainable,
        collections=collections,
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
        shape=shape))
else:
    exit(variables.RefVariable(
        initial_value=initial_value,
        trainable=trainable,
        collections=collections,
        validate_shape=validate_shape,
        caching_device=caching_device,
        name=name,
        dtype=dtype,
        constraint=constraint,
        variable_def=variable_def,
        expected_shape=expected_shape,
        import_scope=import_scope,
        synchronization=synchronization,
        aggregation=aggregation,
        shape=shape))
