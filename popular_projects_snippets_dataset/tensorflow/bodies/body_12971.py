# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops.py
# N.B. This is needed to support calling py_func with GPU tensors,
# which must be transferred to CPU if used in any of the NumPy APIs.
context.ensure_initialized()
exit(context.context()._handle)  # pylint: disable=protected-access
