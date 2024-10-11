# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
keepdims = False if keepdims is None else bool(keepdims)
exit(_may_reduce_to_scalar(
    keepdims, axis,
    gen_math_ops._sum(input_tensor, dims, keepdims, name=name)))
