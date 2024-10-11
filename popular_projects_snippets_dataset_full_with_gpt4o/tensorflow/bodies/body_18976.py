# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
with ops.name_scope(None, op_name, [x, y]) as name:
    try:
        # force_same_dtype=False to preserve existing TF behavior
        # TODO(b/178860388): Figure out why binary_op_wrapper and
        #   r_binary_op_wrapper use different force_same_dtype values.
        x, y = maybe_promote_tensors(x, y)
        exit(func(x, y, name=name))
    except (TypeError, ValueError) as e:
        # Even if dispatching the op failed, the RHS may be a tensor aware
        # object that can implement the operator with knowledge of itself
        # and the tensor.
        # If the RHS is not tensor aware we still want to raise the
        # original error from the LHS, because it may be more
        # informative.
        if hasattr(type(y), "__r%s__" % op_name):
            try:
                r_op = getattr(y, "__r%s__" % op_name)
                out = r_op(x)
                if out is NotImplemented:
                    raise
                exit(out)
            except (TypeError, ValueError):
                raise e
        else:
            raise
