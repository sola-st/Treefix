# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py
with ops.name_scope_v2(self.name or "PiecewiseConstant"):
    boundaries = nest.map_structure(ops.convert_to_tensor_v2_with_dispatch,
                                    nest.flatten(self.boundaries))
    values = nest.map_structure(ops.convert_to_tensor_v2_with_dispatch,
                                nest.flatten(self.values))
    x_recomp = ops.convert_to_tensor_v2_with_dispatch(step)
    for i, b in enumerate(boundaries):
        if b.dtype.base_dtype != x_recomp.dtype.base_dtype:
            # We cast the boundaries to have the same type as the step
            b = math_ops.cast(b, x_recomp.dtype.base_dtype)
            boundaries[i] = b
    pred_fn_pairs = []
    pred_fn_pairs.append((x_recomp <= boundaries[0], lambda: values[0]))
    pred_fn_pairs.append((x_recomp > boundaries[-1], lambda: values[-1]))
    for low, high, v in zip(boundaries[:-1], boundaries[1:], values[1:-1]):
        # Need to bind v here; can do this with lambda v=v: ...
        pred = (x_recomp > low) & (x_recomp <= high)
        pred_fn_pairs.append((pred, lambda v=v: v))

    # The default isn't needed here because our conditions are mutually
    # exclusive and exhaustive, but tf.case requires it.
    default = lambda: values[0]
    exit(control_flow_ops.case(pred_fn_pairs, default, exclusive=True))
