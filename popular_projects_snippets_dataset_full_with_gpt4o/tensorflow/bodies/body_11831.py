# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
exit(control_flow_ops.cond(is_finite,
                             lambda: math_ops.less(i, max_squarings),
                             lambda: constant_op.constant(False)))
