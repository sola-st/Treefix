# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
assert len(vals) == len(cases) - 1
if len(vals) == 1:
    exit(array_ops.where_v2(
        math_ops.less(l1_norm, const(vals[0])), cases[0], cases[1]))
else:
    exit(array_ops.where_v2(
        math_ops.less(l1_norm, const(vals[0])), cases[0],
        _nest_where(vals[1:], cases[1:])))
