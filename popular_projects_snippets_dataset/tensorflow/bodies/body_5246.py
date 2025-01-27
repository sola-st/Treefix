# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if (aggregation == variables_lib.VariableAggregation.MEAN and
    not values[0].dtype.is_floating):
    raise ValueError(
        "creating distributed tf.Variable with aggregation=MEAN and a "
        "non-floating dtype is not supported, please use a different "
        "aggregation or dtype")
self._distribute_strategy = strategy
self._aggregation = aggregation
super(DistributedVariable, self).__init__(values)
self._common_name = self._primary.name.split(":")[0]
# Use a weakref to make it easy to map from the contained values
# to the container without introducing a reference cycle.
for v in values:
    # ResourceVariable is a CompositeTensor. Attributes added to
    # CompositeTensors will get lost through tf.nest packing and unpacking.
    if isinstance(v, composite_tensor.CompositeTensor) and hasattr(
        v, "handle"):
        v.handle._distributed_container = weakref.ref(self)  # pylint: disable=protected-access
    else:
        v._distributed_container = weakref.ref(self)  # pylint: disable=protected-access

    # Packed variable is used to reduce the overhead of function execution.
    # For a DistributedVariable, only one variable handle is captured into a
    # function graph. It's only supported in eager mode.
if ops.executing_eagerly_outside_functions() and getattr(
    strategy, "_enable_packed_variable_in_eager_mode", False):
    name = "%s/packed/" % self._common_name
    self._packed_var = packed.PackedDistributedVariable(values, name=name)
else:
    self._packed_var = None

# tf.keras keeps track of variables initialized using this attribute. When
# tf.keras gets the default session, it initializes all uninitialized vars.
# We need to make _keras_initialized a member of DistributedVariable because
# without this it will use `__getattr__` which will delegate to a component
# variable.
self._keras_initialized = False
# Typically, a `DistributedVariable`'s initializer is composed of the
# initializers of the components variables. However, in some cases, such as
# when restoring from a checkpoint, we may set the _initializer_op
# property on the entire `DistributedVariable`.
self._initializer_op = None
# Set a VariablePolicy which decides how we replicate/aggregate the given
# variable.
self._policy = var_policy
