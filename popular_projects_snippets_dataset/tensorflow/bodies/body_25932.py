# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/readers.py
"""See `tf.data.experimental.parallel_interleave()` for details."""
self._input_dataset = input_dataset
self._map_func = structured_function.StructuredFunctionWrapper(
    map_func, self._transformation_name(), dataset=input_dataset)
if not isinstance(self._map_func.output_structure, dataset_ops.DatasetSpec):
    raise TypeError(
        "The `map_func` argument must return a `Dataset` object. Got "
        f"{_get_type(self._map_func.output_structure)!r}.")
self._element_spec = self._map_func.output_structure._element_spec  # pylint: disable=protected-access
self._cycle_length = ops.convert_to_tensor(
    cycle_length, dtype=dtypes.int64, name="cycle_length")
self._block_length = ops.convert_to_tensor(
    block_length, dtype=dtypes.int64, name="block_length")
self._buffer_output_elements = convert.optional_param_to_tensor(
    "buffer_output_elements",
    buffer_output_elements,
    argument_default=2 * block_length)
self._prefetch_input_elements = convert.optional_param_to_tensor(
    "prefetch_input_elements",
    prefetch_input_elements,
    argument_default=2 * cycle_length)
if sloppy is None:
    self._deterministic = "default"
elif sloppy:
    self._deterministic = "false"
else:
    self._deterministic = "true"
self._name = name

variant_tensor = ged_ops.legacy_parallel_interleave_dataset_v2(
    self._input_dataset._variant_tensor,  # pylint: disable=protected-access
    self._map_func.function.captured_inputs,
    self._cycle_length,
    self._block_length,
    self._buffer_output_elements,
    self._prefetch_input_elements,
    f=self._map_func.function,
    deterministic=self._deterministic,
    **self._common_args)
super(ParallelInterleaveDataset, self).__init__(input_dataset,
                                                variant_tensor)
