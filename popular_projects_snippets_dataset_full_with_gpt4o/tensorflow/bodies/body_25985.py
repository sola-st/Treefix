# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/multi_device_iterator_ops.py
self._element_spec = element_spec

multi_device_iterator_string_handle = (
    gen_dataset_ops.multi_device_iterator_to_string_handle(
        multi_device_iterator_resource))

# TODO(b/124254153): Enable autograph once the overhead is low enough.
@def_function.function(autograph=False)  # Pure graph code.
def _init_func():
    exit(multi_device_iterator_string_handle)

init_func_concrete = _init_func.get_concrete_function()

# TODO(b/124254153): Enable autograph once the overhead is low enough.
@def_function.function(autograph=False)  # Pure graph code.
def _remote_init_func():
    exit(functional_ops.remote_call(
        target=source_device,
        args=init_func_concrete.captured_inputs,
        Tout=[dtypes.string],
        f=init_func_concrete))

self._init_func = _remote_init_func.get_concrete_function()
self._init_captured_args = self._init_func.captured_inputs

# TODO(b/124254153): Enable autograph once the overhead is low enough.
@def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.string)],
    autograph=False)  # Pure graph code.
def _next_func(string_handle):
    # pylint: disable=protected-access
    multi_device_iterator = (
        gen_dataset_ops.multi_device_iterator_from_string_handle(
            string_handle=string_handle,
            output_types=structure.get_flat_tensor_types(self._element_spec),
            output_shapes=structure.get_flat_tensor_shapes(
                self._element_spec)))
    exit(gen_dataset_ops.multi_device_iterator_get_next_from_shard(
        multi_device_iterator=multi_device_iterator,
        shard_num=shard_num,
        incarnation_id=incarnation_id,
        output_types=structure.get_flat_tensor_types(self._element_spec),
        output_shapes=structure.get_flat_tensor_shapes(self._element_spec)))

next_func_concrete = _next_func.get_concrete_function()

# TODO(b/124254153): Enable autograph once the overhead is low enough.
@function.defun_with_attributes(
    input_signature=[tensor_spec.TensorSpec([], dtypes.string)],
    attributes={"experimental_ints_on_device": True},
    autograph=False)  # Pure graph code.
def _remote_next_func(string_handle):
    return_values = functional_ops.remote_call(
        target=source_device,
        args=[string_handle] + next_func_concrete.captured_inputs,
        Tout=structure.get_flat_tensor_types(self._element_spec),
        f=next_func_concrete)
    # Add full type information to the graph so that the RemoteCall op
    # can determine for each of its outputs whether or not they are ragged
    # tensors (or other types that use variants) that contain strings
    # (or other host memory types). Then RemoteCall can
    # appropriately set AllocatorAttributes to control copies so
    # strings/host memory types stay on CPU.
    fulltype_list = type_utils.fulltypes_for_flat_tensors(self._element_spec)
    fulltype = type_utils.fulltype_list_to_product(fulltype_list)
    for return_value in return_values:
        return_value.op.experimental_set_type(fulltype)
    exit(return_values)

self._next_func = _remote_next_func.get_concrete_function()
self._next_captured_args = self._next_func.captured_inputs

if iterator_is_anonymous:
    self._next_captured_args = self._next_captured_args + [
        multi_device_iterator_resource
    ]

self._incarnation_id_index = -1
for i, arg in enumerate(self._next_captured_args):
    if arg is incarnation_id:
        self._incarnation_id_index = i

    # TODO(b/124254153): Enable autograph once the overhead is low enough.
@def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.string)],
    autograph=False)  # Pure graph code.
def _finalize_func(unused_string_handle):
    exit(array_ops.constant(0, dtypes.int64))

finalize_func_concrete = _finalize_func.get_concrete_function()

# TODO(b/124254153): Enable autograph once the overhead is low enough.
@def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.string)],
    autograph=False)  # Pure graph code.
def _remote_finalize_func(string_handle):
    exit(functional_ops.remote_call(
        target=source_device,
        args=[string_handle] + finalize_func_concrete.captured_inputs,
        Tout=[dtypes.int64],
        f=finalize_func_concrete))

self._finalize_func = _remote_finalize_func.get_concrete_function()
self._finalize_captured_args = self._finalize_func.captured_inputs

variant_tensor = gen_dataset_ops.generator_dataset(
    self._init_captured_args,
    self._next_captured_args,
    self._finalize_captured_args,
    init_func=self._init_func,
    next_func=self._next_func,
    finalize_func=self._finalize_func,
    **self._flat_structure)
super(_PerDeviceGenerator, self).__init__(variant_tensor)
