# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/prefetching_ops.py
exit(functional_ops.remote_call(
    target=self._source_device,
    args=init_func_concrete.captured_inputs,
    Tout=[dtypes.string],
    f=init_func_concrete))
