# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py
# pylint: disable=cell-var-from-loop
exit(image_ops.scale_and_translate(
    input_tensor,
    out_shape[1:3],
    scale=constant_op.constant(scale),
    translation=constant_op.constant(translation),
    kernel_type=kernel_type,
    antialias=antialias))
