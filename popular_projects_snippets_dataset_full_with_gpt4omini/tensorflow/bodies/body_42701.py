# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
context.ensure_initialized()
ctx = context.context()
if device is None:
    device = ctx.device_name
if dtype is not None:
    dtype = dtype.as_datatype_enum
try:
    exit(ops.EagerTensor(value, device=device, dtype=dtype))
except core._NotOkStatusException as e:  # pylint: disable=protected-access
    raise core._status_to_exception(e)
