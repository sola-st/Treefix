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
self._name = name
variant_tensor = gen_dataset_ops.interleave_dataset(
    input_dataset._variant_tensor,  # pylint: disable=protected-access
    self._map_func.function.captured_inputs,  # pylint: disable=protected-access
    self._cycle_length,
    self._block_length,
    f=self._map_func.function,
    **self._common_args)
super().__init__(input_dataset, variant_tensor)
