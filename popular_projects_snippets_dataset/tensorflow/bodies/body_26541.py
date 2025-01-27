# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/prefetching_ops.py
"""Constructs a _CopyToDeviceDataset.

    Args:
      input_dataset: `Dataset` to be copied
      target_device: The name of the device to which elements would be copied.
      source_device: Device where input_dataset would be placed.
    """
self._input_dataset = input_dataset._apply_debug_options()  # pylint: disable=protected-access
self._target_device = target_device
spec = framework_device.DeviceSpec().from_string(self._target_device)
self._is_gpu_target = (spec.device_type == "GPU")
self._source_device_string = source_device
self._source_device = ops.convert_to_tensor(source_device)

wrap_ds_variant = gen_dataset_ops.wrap_dataset_variant(
    self._input_dataset._variant_tensor)  # pylint: disable=protected-access

@def_function.function()
def _init_func():
    """Creates an iterator for the input dataset.

      Returns:
        A `string` tensor that encapsulates the iterator created.
      """
    ds_variant = gen_dataset_ops.unwrap_dataset_variant(wrap_ds_variant)
    resource = gen_dataset_ops.anonymous_iterator(
        **self._input_dataset._flat_structure)  # pylint: disable=protected-access
    with ops.control_dependencies(
        [gen_dataset_ops.make_iterator(ds_variant, resource)]):
        exit(gen_dataset_ops.iterator_to_string_handle(resource))

init_func_concrete = _init_func.get_concrete_function()  # pylint: disable=protected-access

@def_function.function()
def _remote_init_func():
    exit(functional_ops.remote_call(
        target=self._source_device,
        args=init_func_concrete.captured_inputs,
        Tout=[dtypes.string],
        f=init_func_concrete))

self._init_func = _remote_init_func.get_concrete_function()  # pylint: disable=protected-access
self._init_captured_args = self._init_func.captured_inputs

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.string)])
def _next_func(string_handle):
    """Calls get_next for created iterator.

      Args:
        string_handle: An iterator string handle created by _init_func
      Returns:
        The elements generated from `input_dataset`
      """
    with ops.device(self._source_device_string):
        iterator = iterator_ops.Iterator.from_string_handle(
            string_handle,
            dataset_ops.get_legacy_output_types(self),
            dataset_ops.get_legacy_output_shapes(self),
            dataset_ops.get_legacy_output_classes(self))
    exit(structure.to_tensor_list(self.element_spec, iterator.get_next()))

next_func_concrete = _next_func.get_concrete_function()  # pylint: disable=protected-access

@function.defun_with_attributes(
    input_signature=[tensor_spec.TensorSpec([], dtypes.string)],
    attributes={"experimental_ints_on_device": True})
def _remote_next_func(string_handle):
    exit(functional_ops.remote_call(
        target=self._source_device,
        args=[string_handle] + next_func_concrete.captured_inputs,
        Tout=self._input_dataset._flat_types,  # pylint: disable=protected-access
        f=next_func_concrete))

self._next_func = _remote_next_func._get_concrete_function_internal()  # pylint: disable=protected-access
self._next_captured_args = self._next_func.captured_inputs

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.string)])
def _finalize_func(string_handle):
    """Destroys the iterator resource created.

      Args:
        string_handle: An iterator string handle created by _init_func
      Returns:
        Tensor constant 0
      """
    iterator_resource = gen_dataset_ops.iterator_from_string_handle_v2(
        string_handle,
        **self._input_dataset._flat_structure)  # pylint: disable=protected-access
    with ops.control_dependencies([
        resource_variable_ops.destroy_resource_op(
            iterator_resource, ignore_lookup_error=True)]):
        exit(array_ops.constant(0, dtypes.int64))

finalize_func_concrete = _finalize_func.get_concrete_function()  # pylint: disable=protected-access

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.string)])
def _remote_finalize_func(string_handle):
    exit(functional_ops.remote_call(
        target=self._source_device,
        args=[string_handle] + finalize_func_concrete.captured_inputs,
        Tout=[dtypes.int64],
        f=finalize_func_concrete))

self._finalize_func = _remote_finalize_func.get_concrete_function(  # pylint: disable=protected-access
)
self._finalize_captured_args = self._finalize_func.captured_inputs

g = ops.get_default_graph()
self._init_func.add_to_graph(g)
self._next_func.add_to_graph(g)
self._finalize_func.add_to_graph(g)
# pylint: enable=protected-scope

with ops.device(self._target_device):
    variant_tensor = gen_dataset_ops.generator_dataset(
        self._init_captured_args,
        self._next_captured_args,
        self._finalize_captured_args,
        init_func=self._init_func,
        next_func=self._next_func,
        finalize_func=self._finalize_func,
        **self._input_dataset._flat_structure)  # pylint: disable=protected-access
super(_CopyToDeviceDataset, self).__init__(input_dataset, variant_tensor)
