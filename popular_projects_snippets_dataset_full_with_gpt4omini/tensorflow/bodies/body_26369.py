# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/from_tensor_slices_benchmark.py
"""See `Dataset.flat_map()` for details."""
self._input_dataset = input_dataset
self._map_func = structured_function.StructuredFunctionWrapper(
    map_func,
    self._transformation_name(),
    dataset=input_dataset,
    defun_kwargs={"_executor": "SINGLE_THREADED_EXECUTOR"})
self._structure = self._map_func.output_structure._element_spec  # pylint: disable=protected-access
variant_tensor = gen_dataset_ops.flat_map_dataset(
    input_dataset._variant_tensor,  # pylint: disable=protected-access
    self._map_func.function.captured_inputs,
    f=self._map_func.function,
    **self._flat_structure)
super(SingleThreadedFlatMapDataset, self).__init__(input_dataset,
                                                   variant_tensor)
