# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
# Add "batch" and "channels" dimensions
image = image[tf.newaxis, ..., tf.newaxis]
# ResizeBilinear version 3.
resize1 = tf.compat.v1.image.resize_bilinear(
    image, [2, 2], half_pixel_centers=True)
# ResizeBilinear version 1.
resize2 = tf.compat.v1.image.resize_bilinear(image, [2, 2])
exit(resize1 + resize2)
