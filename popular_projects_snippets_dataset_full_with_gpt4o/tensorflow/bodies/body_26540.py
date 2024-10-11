# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/prefetching_ops.py
exit(functional_ops.remote_call(
    target=self._source_device,
    args=[string_handle] + finalize_func_concrete.captured_inputs,
    Tout=[dtypes.int64],
    f=finalize_func_concrete))
