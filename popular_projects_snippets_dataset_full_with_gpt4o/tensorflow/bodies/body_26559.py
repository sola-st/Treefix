# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/grouping.py
"""See `group_by_reducer()` for details."""
self._input_dataset = input_dataset
self._make_key_func(key_func, input_dataset)
self._make_init_func(reducer.init_func)
self._make_reduce_func(reducer.reduce_func, input_dataset)
self._make_finalize_func(reducer.finalize_func)
variant_tensor = ged_ops.experimental_group_by_reducer_dataset(
    self._input_dataset._variant_tensor,  # pylint: disable=protected-access
    self._key_func.function.captured_inputs,
    self._init_func.function.captured_inputs,
    self._reduce_func.function.captured_inputs,
    self._finalize_func.function.captured_inputs,
    key_func=self._key_func.function,
    init_func=self._init_func.function,
    reduce_func=self._reduce_func.function,
    finalize_func=self._finalize_func.function,
    **self._flat_structure)
super(_GroupByReducerDataset, self).__init__(input_dataset, variant_tensor)
