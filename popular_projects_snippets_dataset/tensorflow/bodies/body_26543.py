# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/prefetching_ops.py
"""See `Dataset.map()` for details."""
self._input_dataset = input_dataset
self._use_inter_op_parallelism = use_inter_op_parallelism

self._map_func = structured_function.StructuredFunctionWrapper(
    map_func,
    self._transformation_name(),
    dataset=input_dataset,
    defun_kwargs={"experimental_ints_on_device": True})
variant_tensor = ged_ops.experimental_map_dataset(
    self._input_dataset._variant_tensor,  # pylint: disable=protected-access
    self._map_func.function.captured_inputs,
    f=self._map_func.function,
    use_inter_op_parallelism=self._use_inter_op_parallelism,
    **self._flat_structure)
super(_MapOnGpuDataset, self).__init__(input_dataset, variant_tensor)
