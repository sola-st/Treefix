# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/interleave_op.py
"""See `Dataset.interleave()` for details."""
self._input_dataset = input_dataset
self._map_func = structured_function.StructuredFunctionWrapper(
    map_func, self._transformation_name(), dataset=input_dataset)
if not isinstance(self._map_func.output_structure, dataset_ops.DatasetSpec):
    raise TypeError(
        "The `map_func` argument must return a `Dataset` object. Got "
        f"{dataset_ops.get_type(self._map_func.output_structure)!r}.")
self._structure = self._map_func.output_structure._element_spec  # pylint: disable=protected-access
self._cycle_length = ops.convert_to_tensor(
    cycle_length, dtype=dtypes.int64, name="cycle_length")
self._block_length = ops.convert_to_tensor(
    block_length, dtype=dtypes.int64, name="block_length")
self._buffer_output_elements = ops.convert_to_tensor(
    buffer_output_elements,
    dtype=dtypes.int64,
    name="buffer_output_elements")
self._prefetch_input_elements = ops.convert_to_tensor(
    prefetch_input_elements,
    dtype=dtypes.int64,
    name="prefetch_input_elements")

self._num_parallel_calls = ops.convert_to_tensor(
    num_parallel_calls, dtype=dtypes.int64, name="num_parallel_calls")
if deterministic is None:
    deterministic_string = "default"
elif deterministic:
    deterministic_string = "true"
else:
    deterministic_string = "false"

self._name = name
variant_tensor = gen_dataset_ops.parallel_interleave_dataset_v4(
    input_dataset._variant_tensor,  # pylint: disable=protected-access
    self._map_func.function.captured_inputs,  # pylint: disable=protected-access
    self._cycle_length,
    self._block_length,
    self._buffer_output_elements,
    self._prefetch_input_elements,
    self._num_parallel_calls,
    f=self._map_func.function,
    deterministic=deterministic_string,
    **self._common_args)
super().__init__(input_dataset, variant_tensor)
