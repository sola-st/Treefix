# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
for (t, shape, input_t) in zip(flat_output_tensors, flat_shape_invariants,
                               flat_input_tensors):
    if not control_flow_ops._ShapeLessThanOrEqual(t.shape, shape):
        raise ValueError(
            f"Input tensor `{input_t.name}` enters the loop with shape {shape}, "
            f"but has shape {t.shape} after one iteration. To allow the shape to "
            "vary across iterations, use the `shape_invariants` argument of "
            "tf.while_loop to specify a less-specific shape.")
