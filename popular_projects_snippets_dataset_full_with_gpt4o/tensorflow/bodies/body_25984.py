# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/multi_device_iterator_ops.py
exit(functional_ops.remote_call(
    target=source_device,
    args=[string_handle] + finalize_func_concrete.captured_inputs,
    Tout=[dtypes.int64],
    f=finalize_func_concrete))
