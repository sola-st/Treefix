# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/group_by_window_op.py
"""See `group_by_window()` for details."""
self._input_dataset = input_dataset
self._make_key_func(key_func, input_dataset)
self._make_reduce_func(reduce_func, input_dataset)
self._make_window_size_func(window_size_func)
self._name = name
variant_tensor = ged_ops.group_by_window_dataset(
    self._input_dataset._variant_tensor,  # pylint: disable=protected-access
    self._key_func.function.captured_inputs,
    self._reduce_func.function.captured_inputs,
    self._window_size_func.function.captured_inputs,
    key_func=self._key_func.function,
    reduce_func=self._reduce_func.function,
    window_size_func=self._window_size_func.function,
    **self._common_args)
super().__init__(input_dataset, variant_tensor)
