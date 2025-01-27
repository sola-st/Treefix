# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/multi_device_iterator_ops.py
exit(functional_ops.remote_call(
    target=source_device,
    args=init_func_concrete.captured_inputs,
    Tout=[dtypes.string],
    f=init_func_concrete))
