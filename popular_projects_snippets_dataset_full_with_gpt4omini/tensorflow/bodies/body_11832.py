# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
exit((i + 1, array_ops.where_v2(
    math_ops.less(i, squarings), math_ops.matmul(r, r), r)))
