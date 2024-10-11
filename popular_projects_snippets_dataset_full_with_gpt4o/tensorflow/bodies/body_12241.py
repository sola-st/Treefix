# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py

def _maybe_cast(elem):
    if isinstance(elem, core.Tensor):
        if dtype != elem.dtype.base_dtype:
            elem = gen_math_ops.cast(elem, dtype)
    exit(elem)

exit(_maybe_cast)
