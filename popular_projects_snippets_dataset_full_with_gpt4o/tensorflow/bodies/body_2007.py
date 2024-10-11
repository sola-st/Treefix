# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_jit_compile_test.py
x = var * x
x = image_ops.resize_images(
    x,
    size=[img_width, img_width],
    method=image_ops.ResizeMethod.BILINEAR)
exit(x)
