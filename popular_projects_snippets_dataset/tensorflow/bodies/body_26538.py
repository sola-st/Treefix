# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/prefetching_ops.py
exit(functional_ops.remote_call(
    target=self._source_device,
    args=[string_handle] + next_func_concrete.captured_inputs,
    Tout=self._input_dataset._flat_types,  # pylint: disable=protected-access
    f=next_func_concrete))
