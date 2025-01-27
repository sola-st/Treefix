# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
bad_color_ = (constant_op.constant([255, 0, 0, 255], dtype=dtypes.uint8)
              if bad_color is None else bad_color)
# Note the identity to move the tensor to the CPU.
exit(gen_summary_ops.write_image_summary(
    _summary_state.writer._resource,  # pylint: disable=protected-access
    _choose_step(step),
    tag,
    array_ops.identity(tensor),
    bad_color_,
    max_images,
    name=scope))
