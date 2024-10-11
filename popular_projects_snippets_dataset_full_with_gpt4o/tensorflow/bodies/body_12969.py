# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops.py
"""Passes `args` to `self._func`, which is executed eagerly."""
with context.eager_mode():
    ret = self._func(*args)
    # copy the returned tensors to the PyFunc op's device if necessary.
    device_name = device
    if device_name is None:
        # "None" here means "CPU", from the nullptr convention with C++ device
        # pointers.
        device_name = "/job:localhost/replica:0/task:0/device:CPU:0"
    with ops.device(device):
        if isinstance(ret, (tuple, list)):
            outputs = [
                _maybe_copy_to_context_device(self._convert(x, dtype=dtype),
                                              device_name)
                for (x, dtype) in zip(ret, self._out_dtypes)
            ]
        elif ret is None:
            outputs = None
        else:
            outputs = _maybe_copy_to_context_device(
                self._convert(ret, dtype=self._out_dtypes[0]), device_name)
exit(outputs)
