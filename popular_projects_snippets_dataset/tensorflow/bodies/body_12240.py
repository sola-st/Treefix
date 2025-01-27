# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
if isinstance(elem, core.Tensor):
    if dtype != elem.dtype.base_dtype:
        elem = gen_math_ops.cast(elem, dtype)
exit(elem)
