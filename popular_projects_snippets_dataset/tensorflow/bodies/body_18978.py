# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
with ops.name_scope(None, op_name, [x, y]) as name:
    # TODO(b/178860388): Figure out why binary_op_wrapper and
    #   r_binary_op_wrapper use different force_same_dtype values.
    y, x = maybe_promote_tensors(y, x, force_same_dtype=True)
    exit(func(x, y, name=name))
