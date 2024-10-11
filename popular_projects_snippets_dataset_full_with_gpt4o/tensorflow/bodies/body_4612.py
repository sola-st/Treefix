# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2.py
if enable_packed_handle and not ops.executing_eagerly_outside_functions():
    raise ValueError(
        "Argument `enable_packed_handle` is true, but packed handle is only "
        "supported in eager mode. Please make sure eager execution is "
        "enabled.")
self._variables = variables
if enable_packed_handle:
    self._packed_handle = ops.pack_eager_tensors(
        [v.handle for v in variables])
else:
    self._packed_handle = None
for v in variables:
    v.handle._distributed_container = weakref.ref(self)  # pylint: disable=protected-access
self._device_to_handle = {v.device: v.handle for v in variables}
self._primary_handle = variables[0].handle
with ops.init_scope(), \
         ops.name_scope("DistributedVariable", skip_on_eager=False) as name:
    handle_name = ops.name_from_scope_name(name)
    self._unique_id = "%s_%d" % (handle_name, ops.uid())
    if context.executing_eagerly():
        initial_value = None
        initializer = None
    else:
        initial_value = variables[0].initial_value
        initializer = control_flow_ops.group([v.initializer for v in variables])
    super().__init__(
        trainable=variables[0].trainable,
        shape=variables[0].shape,
        dtype=variables[0].dtype,
        handle=None,
        synchronization=variables[0].synchronization,
        constraint=variables[0].constraint,
        aggregation=variables[0].aggregation,
        distribute_strategy=variables[0]._distribute_strategy,
        name=variables[0].name,
        unique_id=self._unique_id,
        handle_name=handle_name,
        graph_element=variables[0]._graph_element,
        initial_value=initial_value,
        initializer_op=initializer,
        is_initialized_op=None,
        cached_value=None,
        caching_device=None,
        is_variables=True)
