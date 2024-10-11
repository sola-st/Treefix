# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/resize_bilinear.py
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input",
    shape=parameters["input_shape"])
out = tf.compat.v1.image.resize_bilinear(
    input_tensor,
    size=parameters["size"],
    align_corners=parameters["align_corners"],
    half_pixel_centers=parameters["half_pixel_centers"])
exit(([input_tensor], [out]))
